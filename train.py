"""
ScamShield AI - Kịch bản huấn luyện (Train) tối ưu cho Google Colab
Khắc phục 100% lỗi lệch dữ liệu (Imbalanced Data) bằng WeightedRandomSampler
"""

import json, os, re, random
import torch
import numpy as np
from torch.utils.data import Dataset, DataLoader, WeightedRandomSampler
from transformers import AutoTokenizer, AutoModelForSequenceClassification, AdamW
from sklearn.metrics import classification_report, f1_score
from sklearn.model_selection import train_test_split

# 1. CẤU HÌNH (CONFIG)

SCAM_FILE      = "tong_hop_dataset.json"
HARMLESS_FILE  = "tong_hop_dataset(antoan).json"
SAVE_DIR       = "./saved_model"
MODEL_NAME     = "vinai/phobert-base-v2"

MAX_LEN        = 256
BATCH_SIZE     = 16
EPOCHS         = 15   # 15 Epoch là đủ vì có Early Stopping
LEARNING_RATE  = 2e-5
HARMLESS_CAP   = 650  # Ép số lượng nhãn An toàn xuống để cân bằng

DEVICE = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print(f"[INFO] Thiết bị đang dùng: {DEVICE}")


# 2. XỬ LÝ DỮ LIỆU & FIX LỖI TYPO

def normalize_text(text):
    text = str(text).replace("\r", " ").replace("\n", " ")
    return re.sub(r"\s+", " ", text).strip()

def parse_dialogue(item):
    dialogue = item.get("dialogue", "")
    if isinstance(dialogue, list):
        # Lấy 8 lượt thoại cuối (Scam thường lộ ở phần cuối)
        tail_turns = dialogue[-8:] if len(dialogue) > 8 else dialogue
        parts = []
        for t in tail_turns:
            if isinstance(t, dict):
                parts.append(f"{t.get('role', '')}: {t.get('content', '')}")
            else:
                parts.append(str(t))
        return normalize_text(" [SEP] ".join(parts))
    return normalize_text(dialogue)

# Đọc dữ liệu Scam
try:
    with open(SCAM_FILE, "r", encoding="utf-8") as f:
        scam_data = json.load(f)
except FileNotFoundError:
    print(f"[LỖI] Không tìm thấy file {SCAM_FILE}. Hãy upload lên Colab nhé!")
    scam_data = []

# Đọc dữ liệu An toàn
try:
    with open(HARMLESS_FILE, "r", encoding="utf-8") as f:
        harmless_data = json.load(f)
except FileNotFoundError:
    print(f"[LỖI] Không tìm thấy file {HARMLESS_FILE}.")
    harmless_data = []

dataset_texts = []
dataset_labels = []
label_map = {0: "Khong phai lua dao"}

# Đưa data lừa đảo vào mảng
for item in scam_data:
    text = parse_dialogue(item)
    if not text: continue

    label_id = item.get("label", -1)
    label_name = item.get("label_name", f"Scam {label_id}")

    # [FIX LỖI DATA] Sửa lỗi gõ sai tên nhãn (thiếu dấu phẩy)
    if "Lừa đảo mở rút tiền" in label_name:
        label_name = "Lừa đảo mở, rút tiền thẻ tín dụng"

    label_map[label_id] = label_name
    dataset_texts.append(text)
    dataset_labels.append(label_id)

# Lọc và đưa data An toàn vào mảng (Capping 650 mẫu)
random.seed(42)
random.shuffle(harmless_data)
for item in harmless_data[:HARMLESS_CAP]:
    text = parse_dialogue(item)
    if text:
        dataset_texts.append(text)
        dataset_labels.append(0)

NUM_LABELS = max(label_map.keys()) + 1
print(f"[DATA] Tổng số mẫu: {len(dataset_texts)}")
print(f"[DATA] Lừa đảo: {len(scam_data)} | An toàn: {len(dataset_labels) - len(scam_data)}")


# 3. THUẬT TOÁN CÂN BẰNG DATA (CHỐNG LỆCH NHÃN)

def get_balanced_sampler(labels):
    labels_arr = np.array(labels)
    class_counts = np.bincount(labels_arr, minlength=NUM_LABELS)

    weights = []
    for l in labels:
        # Nhãn nào càng ít data, trọng số bốc trúng càng cao
        weight = 1.0 / class_counts[l] if class_counts[l] > 0 else 0
        weights.append(weight)

    return WeightedRandomSampler(weights=weights, num_samples=len(weights), replacement=True)


# 4. CHUẨN BỊ PYTORCH DATASET

class ScamDataset(Dataset):
    def __init__(self, texts, labels, tokenizer):
        self.texts = texts
        self.labels = labels
        self.tokenizer = tokenizer

    def __len__(self):
        return len(self.labels)

    def __getitem__(self, idx):
        enc = self.tokenizer(
            self.texts[idx],
            truncation=True,
            padding="max_length",
            max_length=MAX_LEN,
            return_tensors="pt"
        )
        return {
            "input_ids": enc["input_ids"].squeeze(0),
            "attention_mask": enc["attention_mask"].squeeze(0),
            "labels": torch.tensor(self.labels[idx], dtype=torch.long)
        }

# Chia tập Train/Val (80/20)
train_texts, val_texts, train_labels, val_labels = train_test_split(
    dataset_texts, dataset_labels, test_size=0.15, random_state=42, stratify=dataset_labels
)

print("[INFO] Đang tải Tokenizer...")
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

train_dataset = ScamDataset(train_texts, train_labels, tokenizer)
val_dataset   = ScamDataset(val_texts, val_labels, tokenizer)

# Áp dụng bộ Sampler chống lệch data vào tập Train
train_sampler = get_balanced_sampler(train_labels)
train_loader  = DataLoader(train_dataset, batch_size=BATCH_SIZE, sampler=train_sampler)
val_loader    = DataLoader(val_dataset, batch_size=BATCH_SIZE, shuffle=False)


# 5. KHỞI TẠO MODEL PHOBERT

print("[INFO] Đang tải Model PhoBERT...")
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME, num_labels=NUM_LABELS)

# Đóng băng (Freeze) 6 lớp đầu tiên để model giữ được tiếng Việt gốc và học nhanh hơn
for param in model.roberta.embeddings.parameters():
    param.requires_grad = False
for i in range(6):
    for param in model.roberta.encoder.layer[i].parameters():
        param.requires_grad = False

model.to(DEVICE)
optimizer = AdamW(filter(lambda p: p.requires_grad, model.parameters()), lr=LEARNING_RATE)
loss_fn = torch.nn.CrossEntropyLoss() # Đã cân bằng bằng Sampler nên dùng Loss chuẩn


# 6. VÒNG LẶP HUẤN LUYỆN (TRAINING LOOP)

print(f"\\n{'='*50}\\n BẮT ĐẦU HUẤN LUYỆN MODEL\\n{'='*50}")

best_f1 = 0.0
patience = 4
patience_counter = 0

for epoch in range(EPOCHS):
    model.train()
    total_loss = 0

    for batch in train_loader:
        input_ids = batch["input_ids"].to(DEVICE)
        attention_mask = batch["attention_mask"].to(DEVICE)
        labels = batch["labels"].to(DEVICE)

        optimizer.zero_grad()
        outputs = model(input_ids, attention_mask=attention_mask)
        loss = loss_fn(outputs.logits, labels)
        loss.backward()
        optimizer.step()

        total_loss += loss.item()

    avg_train_loss = total_loss / len(train_loader)

    # Đánh giá trên tập Validation
    model.eval()
    all_preds = []
    all_labels = []

    with torch.no_grad():
        for batch in val_loader:
            input_ids = batch["input_ids"].to(DEVICE)
            attention_mask = batch["attention_mask"].to(DEVICE)
            labels = batch["labels"].to(DEVICE)

            outputs = model(input_ids, attention_mask=attention_mask)
            preds = torch.argmax(outputs.logits, dim=-1)

            all_preds.extend(preds.cpu().numpy())
            all_labels.extend(labels.cpu().numpy())

    val_macro_f1 = f1_score(all_labels, all_preds, average='macro', zero_division=0)

    print(f"Epoch {epoch+1}/{EPOCHS} | Train Loss: {avg_train_loss:.4f} | Val Macro-F1: {val_macro_f1:.4f}")

    # Lưu model nếu tốt hơn
    if val_macro_f1 > best_f1:
        best_f1 = val_macro_f1
        patience_counter = 0
        os.makedirs(SAVE_DIR, exist_ok=True)
        model.save_pretrained(SAVE_DIR)
        tokenizer.save_pretrained(SAVE_DIR)

        # Lưu file meta.json cho backend
        meta = {
            "id2label": {str(k): v for k, v in label_map.items()},
            "conf_threshold": 0.50
        }
        with open(os.path.join(SAVE_DIR, "meta.json"), "w", encoding="utf-8") as f:
            json.dump(meta, f, ensure_ascii=False, indent=2)
        print(f"  -> [ĐÃ LƯU] Đạt kỷ lục mới: F1 = {best_f1:.4f}")
    else:
        patience_counter += 1
        if patience_counter >= patience:
            print(f"\\n[INFO] Dừng sớm tại Epoch {epoch+1} (Early Stopping) vì không cải thiện.")
            break


# 7. BÁO CÁO KẾT QUẢ

print(f"\\n{'='*50}\\n BÁO CÁO PHÂN LOẠI CHI TIẾT (TẬP VALIDATION)\\n{'='*50}")
target_names = [label_map[i] for i in range(NUM_LABELS)]
print(classification_report(all_labels, all_preds, target_names=target_names, zero_division=0))

print(f"\\n[HOÀN TẤT] Model xuất sắc nhất đã được lưu tại thư mục: {SAVE_DIR}")
print("Hãy nén thư mục này lại (zip) và tải về máy tính của bạn!")