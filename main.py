"""
ScamShield AI — Backend v4.0
FastAPI + PhoBERT + Gemini + Auth (JWT) + SQLite

Endpoints mới thêm:
  POST /auth/register   → tạo tài khoản
  POST /auth/login      → đăng nhập, trả JWT
  GET  /auth/me         → thông tin user hiện tại (cần token)
  POST /save-report     → lưu kết quả phân tích vào DB (cần token)
  GET  /my-reports      → lấy lịch sử phân tích của user (cần token)
  DELETE /my-reports/{id} → xóa 1 bản ghi (cần token, chỉ xóa của mình)

SQLite file: scamshield.db (tự tạo khi chạy lần đầu)

Cài thêm:
  pip install python-jose[cryptography] passlib[bcrypt] python-multipart

Run:
  python -m uvicorn main:app --host 127.0.0.1 --port 8000 
"""

import os, re, json, unicodedata, sqlite3, time
from contextlib import contextmanager
from datetime import datetime, timedelta, timezone
from typing import List, Optional

import torch
import numpy as np
from fastapi import FastAPI, HTTPException, UploadFile, File, Depends, status
from fastapi.middleware.cors import CORSMiddleware
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel, EmailStr
import base64
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import google.generativeai as genai


from jose import JWTError, jwt
# from passlib.context import CryptContext
import bcrypt


SAVE_DIR   = "./saved_model"
MAX_LEN    = 256
MAX_TURNS  = 8
DEVICE     = torch.device("cuda" if torch.cuda.is_available() else "cpu")
GEMINI_KEY = "AIzaSyB67vJQH8fi796f--UUByqLjl_XM3Tw2as"

CONF_THRESHOLD = 0.50


# QUAN TRỌNG: đổi SECRET_KEY thành chuỗi ngẫu nhiên dài trước khi deploy!
SECRET_KEY     = "SCAMSHIELD_SUPER_SECRET_KEY_CHANGE_ME_IN_PRODUCTION_2025"
ALGORITHM      = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 60 * 24 * 7   # 7 ngày

DB_FILE = r"C:\Users\NGO BA NAM\.scamshield\scamshield.db"
os.makedirs(os.path.dirname(DB_FILE), exist_ok=True)


# LABEL MAP

ID2LABEL = {
    0:  "Khong phai lua dao",
    1:  "Lua dao dat ban an",
    2:  "Lua dao dat phong khach san",
    3:  "Lua dao dinh danh CCCD",
    4:  "Lua dao gia co quan nha nuoc",
    5:  "Lua dao gia danh co quan thue",
    6:  "Lua dao gia danh cong an",
    7:  "Lua dao gia mao thuong hieu",
    8:  "Lua dao gia san TMDT",
    9:  "Lua dao giao don hang khong co thuc",
    10: "Lua dao hai quan nop phat",
    11: "Lua dao khoa SIM",
    12: "Lua dao may loc nuoc",
    13: "Lua dao mo rut tien the tin dung",
    14: "Lua dao PCCC",
    15: "Lua dao su dung trang web gia mao",
    16: "Lua dao ung dung vi dien tu",
    17: "Lua dao tro cap an sinh xa hoi",
    18: "Lua dao vay von",
    19: "Lua dao cai ung dung doc hai",
    20: "Lua dao loi dung su co ATTT",
    21: "Lua dao bao loi tai khoan",
    22: "Lua dao tu thien",
    23: "Lua dao mao danh nguoi than",
    24: "Lua dao lay lai tien bi lua",
    25: "Lua dao de doa tong tien",
    26: "Lua dao tuyen dung gia",
    27: "Lua dao thanh toan tien giao hang",
    28: "Lua dao dau tu tien ao",
    29: "Lua dao mao danh bac si",
}

SCAM_CATEGORIES = [v for k, v in ID2LABEL.items() if k != 0]

SCAM_SIGNALS = {
    "phi ho so|phi kich hoat|phi bao hiem|dong phi truoc|giai ngan|tin chap|khong the chap": "vay_von",
    "OTP|ma xac nhan|so the|CVV|dao han the|han muc": "the_tin_dung",
    "tai app|cai app|file apk|unknown sources|TeamViewer|cap quyen": "cai_app",
    "bitcoin|crypto|token|staking|NFT|loi nhuan.*%|bot trading|san dau tu": "dau_tu_tien_ao",
    "bi dieu tra|lenh bat|tam giam|bao lanh|Vien Kiem Sat|Bo Cong An|tien ky quy": "gia_cong_an",
    "don hang.*loi|hoan tien|tai khoan bi khoa|xac minh tai khoan|Shopee|Lazada|Tiki": "san_tmdt",
    "trung thuong|phi van chuyen|phi thue|giai thuong|xe may|iPhone": "gia_thuong_hieu",
    "buu pham|phi thong quan|hai quan|tieu huy|luu kho|phi kiem dich": "giao_hang",
    "CCCD.*gui|selfie.*CCCD|dinh danh|sinh trac|VNeID|trung thong tin": "cccd",
    "deepfake|tong tien|video nhay cam|chuyen.*trieu|phat tan": "tong_tien",
    "lam tai nha|luong.*trieu|phi dao tao|phi dang ky|cong tac vien|dat don": "tuyen_dung",
    "zalo.*gui CCCD|ket ban zalo|link.*dang nhap|mat khau cu|domain": "web_gia",
}


# DATABASE — SQLite

def get_db_conn():
    conn = sqlite3.connect(DB_FILE, check_same_thread=False)
    conn.row_factory = sqlite3.Row   # trả về dict-like rows
    conn.execute("PRAGMA journal_mode=WAL")   # hiệu năng tốt hơn với concurrent
    return conn

@contextmanager
def db():
    conn = get_db_conn()
    try:
        yield conn
        conn.commit()
    except Exception:
        conn.rollback()
        raise
    finally:
        conn.close()

def init_db():
    """Tạo bảng nếu chưa tồn tại."""
    with db() as conn:
        conn.executescript("""
            CREATE TABLE IF NOT EXISTS users (
                id         INTEGER PRIMARY KEY AUTOINCREMENT,
                username   TEXT    NOT NULL,
                email      TEXT    NOT NULL UNIQUE,
                hashed_pw  TEXT    NOT NULL,
                created_at TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE TABLE IF NOT EXISTS reports (
                id           INTEGER PRIMARY KEY AUTOINCREMENT,
                user_id      INTEGER NOT NULL REFERENCES users(id) ON DELETE CASCADE,
                is_scam      INTEGER NOT NULL,          -- 0 / 1
                risk_score   INTEGER NOT NULL,
                confidence   REAL    NOT NULL,
                label_name   TEXT    NOT NULL,
                input_text   TEXT,                      -- preview (max 500 chars)
                explanation  TEXT,                      -- JSON string
                created_at   TEXT    NOT NULL DEFAULT (datetime('now'))
            );

            CREATE INDEX IF NOT EXISTS idx_reports_user ON reports(user_id);
            CREATE INDEX IF NOT EXISTS idx_reports_created ON reports(created_at DESC);
        """)
    print("[OK] SQLite DB sẵn sàng:", DB_FILE)


# PASSWORD HASHING
# pwd_ctx = CryptContext(schemes=["bcrypt"], deprecated="auto")

def hash_password(plain: str) -> str:
    # Mã hóa mật khẩu thành bytes, tạo salt và băm
    pwd_bytes = plain.encode('utf-8')
    salt = bcrypt.gensalt()
    hashed_bytes = bcrypt.hashpw(pwd_bytes, salt)
    return hashed_bytes.decode('utf-8')

def verify_password(plain: str, hashed: str) -> bool:
    # So sánh mật khẩu người dùng nhập với chuỗi băm trong Database
    pwd_bytes = plain.encode('utf-8')
    hashed_bytes = hashed.encode('utf-8')
    return bcrypt.checkpw(pwd_bytes, hashed_bytes)


# JWT HELPERS

def create_access_token(user_id: int, email: str) -> str:
    expire = datetime.now(timezone.utc) + timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    payload = {"sub": str(user_id), "email": email, "exp": expire}
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")

def get_current_user(token: str = Depends(oauth2_scheme)) -> dict:
    """Dependency — giải mã JWT, trả dict user. Raise 401 nếu sai."""
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail="Token không hợp lệ hoặc đã hết hạn.",
        headers={"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        user_id: str = payload.get("sub")
        email: str   = payload.get("email")
        if user_id is None:
            raise credentials_exception
    except JWTError:
        raise credentials_exception

    with db() as conn:
        row = conn.execute(
            "SELECT id, username, email FROM users WHERE id = ?", (int(user_id),)
        ).fetchone()
    if row is None:
        raise credentials_exception
    return {"id": row["id"], "username": row["username"], "email": row["email"]}

def get_current_user_optional(token: str = Depends(oauth2_scheme)) -> Optional[dict]:
    """Dependency tuỳ chọn — không raise nếu không có token."""
    try:
        return get_current_user(token)
    except Exception:
        return None


# PHOBERT + GEMINI (giữ nguyên từ v3)

tokenizer_model = None
phobert         = None
gemini_m        = None

def load_models():
    global tokenizer_model, phobert, gemini_m, ID2LABEL, SCAM_CATEGORIES, CONF_THRESHOLD

    meta_path = os.path.join(SAVE_DIR, "meta.json")
    if os.path.isfile(meta_path):
        try:
            with open(meta_path, "r", encoding="utf-8") as f:
                meta = json.load(f)
            ID2LABEL        = {int(k): v for k, v in meta["id2label"].items()}
            SCAM_CATEGORIES = [v for k, v in ID2LABEL.items() if k != 0]
            CONF_THRESHOLD  = meta.get("conf_threshold", 0.50)
            print(f"[OK] meta.json: {len(ID2LABEL)} nhãn, threshold={CONF_THRESHOLD}")
        except Exception as e:
            print(f"[WARN] Đọc meta.json lỗi: {e}")

    if os.path.isdir(SAVE_DIR):
        try:
            tokenizer_model = AutoTokenizer.from_pretrained(SAVE_DIR)
            phobert = AutoModelForSequenceClassification.from_pretrained(SAVE_DIR).to(DEVICE)
            phobert.eval()
            print(f"[OK] PhoBERT loaded ({phobert.config.num_labels} nhãn) on {DEVICE}")
        except Exception as e:
            print(f"[WARN] PhoBERT load failed: {e}")

    if GEMINI_KEY:
        try:
            genai.configure(api_key=GEMINI_KEY)
            gemini_m = genai.GenerativeModel("gemini-2.5-flash-lite")
            print("[OK] Gemini ready")
        except Exception as e:
            print(f"[WARN] Gemini init failed: {e}")

# ── Text utils

def normalize(text: str) -> str:
    text = unicodedata.normalize("NFC", text)
    return re.sub(r"\s+", " ", text).strip()

def dialogue_to_text(turns: list) -> str:
    parts    = []
    selected = turns[-MAX_TURNS:] if len(turns) > MAX_TURNS else turns
    for t in selected:
        role    = t.get("role", "")
        content = normalize(t.get("content", ""))
        label   = "A" if "goi" in role else "B"
        if content:
            parts.append(f"{label}: {content}")
    return " [SEP] ".join(parts)

def split_sentences(text: str) -> List[str]:
    sents = re.split(r'(?<=[.!?])\s+|\[SEP\]', text)
    return [s.strip() for s in sents if s and len(s.strip()) > 10]

def highlight_dangerous(text: str) -> List[dict]:
    medium_kw = ["link", "chuyen khoan", "tai khoan", "xac nhan",
                 "mien phi", "uu dai", "duyet ngay", "gap", "ngay hom nay"]
    results = []
    for sent in split_sentences(text):
        danger     = 0
        sent_lower = sent.lower()
        for pattern in SCAM_SIGNALS:
            if re.search(pattern, sent_lower, re.IGNORECASE):
                danger = 2; break
        if danger == 0 and any(k in sent_lower for k in medium_kw):
            danger = 1
        results.append({"text": sent, "danger": danger})
    return results

def predict(text: str) -> dict:
    if phobert is None or tokenizer_model is None:
        text_lower = text.lower()
        for pattern in SCAM_SIGNALS:
            if re.search(pattern, text_lower, re.IGNORECASE):
                return {
                    "label": 1, "label_name": list(ID2LABEL.values())[1],
                    "confidence": 0.75, "is_scam": True, "is_uncertain": True,
                    "scam_prob": 0.75,
                    "top3": {list(ID2LABEL.values())[1]: 0.75, ID2LABEL[0]: 0.25},
                }
        return {
            "label": 0, "label_name": ID2LABEL[0],
            "confidence": 0.85, "is_scam": False, "is_uncertain": False,
            "scam_prob": 0.15,
            "top3": {ID2LABEL[0]: 0.85, list(ID2LABEL.values())[1]: 0.15},
        }

    enc = tokenizer_model(
        text, truncation=True, padding="max_length",
        max_length=MAX_LEN, return_tensors="pt"
    )
    enc = {k: v.to(DEVICE) for k, v in enc.items()}
    with torch.no_grad():
        probs = torch.softmax(phobert(**enc).logits, dim=-1).squeeze().cpu().numpy()

    pred_label = int(np.argmax(probs))
    confidence = float(probs[pred_label])
    is_scam    = pred_label != 0
    scam_prob  = float(1.0 - probs[0])

    # ── KEYWORD MAP

    LABEL_KEYWORDS = {
        1:  ["đặt bàn", "dat ban", "nhà hàng", "nha hang", "giữ chỗ", "giu cho", "đặt chỗ"],
        2:  ["đặt phòng", "dat phong", "khách sạn", "khach san", "resort", "booking"],
        3:  ["cccd", "căn cước", "can cuoc", "selfie", "định danh", "dinh danh", "vneid"],
        4:  ["bộ công thương", "thanh tra", "cơ quan nhà nước", "ký quỹ", "vi phạm hành chính"],
        5:  ["thuế", "thue", "nợ thuế", "no thue", "kê khai", "ke khai", "cục thuế"],
        6:  ["công an", "cong an", "bắt giam", "bat giam", "bảo lãnh", "bao lanh", "khởi tố", "tam giam"],
        7:  ["trúng thưởng", "trung thuong", "phí vận chuyển", "phi van chuyen", "vinamilk", "honda", "iphone"],
        8:  ["shopee", "lazada", "tiki", "hoàn tiền", "hoan tien", "đơn hàng lỗi", "don hang loi"],
        9:  ["bưu phẩm", "buu pham", "kiện hàng", "kien hang", "phí thông quan", "phi thong quan"],
        10: ["hải quan", "hai quan", "thông quan", "thong quan", "cửa khẩu"],
        11: ["sim", "khóa sim", "khoa sim", "nhà mạng", "nha mang", "viettel", "chuẩn hóa"],
        12: ["máy lọc nước", "may loc nuoc", "lõi lọc", "loi loc", "bảo dưỡng", "kangaroo"],
        13: ["thẻ tín dụng", "the tin dung", "cvv", "đáo hạn", "dao han", "rút tiền mặt"],
        14: ["pccc", "phòng cháy", "phong chay", "bình chữa cháy", "binh chua chay"],
        15: ["link", "website", "đăng nhập", "dang nhap", "domain", "http", "url"],
        16: ["momo", "zalopay", "ví điện tử", "vi dien tu", "thiết bị lạ", "thiet bi la"],
        17: ["bhxh", "trợ cấp", "tro cap", "an sinh", "hộ nghèo", "ho ngheo"],
        18: ["vay", "tín chấp", "tin chap", "giải ngân", "giai ngan", "phí hồ sơ", "phi ho so", "lãi suất"],
        19: ["apk", "cài app", "cai app", "unknown sources", "teamviewer", "cấp quyền"],
        20: ["rò rỉ", "ro ri", "bị hack", "bi hack", "đổi mật khẩu", "doi mat khau", "tấn công"],
        21: ["tài khoản lỗi", "tai khoan loi", "mở khóa", "mo khoa", "inactive", "bị khóa"],
        22: ["từ thiện", "tu thien", "quyên góp", "quyen gop", "ung hộ", "ung ho", "bệnh nhân"],
        23: ["con đây", "con day", "tai nạn", "tai nan", "mượn tiền", "muon tien", "điện thoại hỏng"],
        24: ["lấy lại tiền", "lay lai tien", "thu hồi", "thu hoi", "phí điều tra", "phi dieu tra"],
        25: ["video nhạy cảm", "video nhay cam", "tống tiền", "tong tien", "phát tán", "phat tan"],
        26: ["tuyển dụng", "tuyen dung", "làm tại nhà", "lam tai nha", "phí đào tạo", "phi dao tao"],
        27: ["cod", "ship", "shipper", "thanh toán trước", "thanh toan truoc", "phí giao hàng"],
        28: ["bitcoin", "crypto", "token", "nft", "staking", "bot trading", "sàn đầu tư", "lợi nhuận"],
        29: ["bác sĩ", "bac si", "xét nghiệm", "xet nghiem", "ung thư", "ung thu", "thuốc đặc trị"],
    }

    text_lower = text.lower()

    def has_keywords(label_id: int) -> bool:
        keywords = LABEL_KEYWORDS.get(label_id, [])
        return any(kw in text_lower for kw in keywords)

    final_label  = pred_label
    is_uncertain = False

    if pred_label != 0 and not has_keywords(pred_label):
        top10_idx = [int(i) for i in np.argsort(probs)[::-1][:10]]
        best_label, best_prob = None, 0.0

        for idx in top10_idx:
            if idx == 0:
                continue
            if has_keywords(idx) and float(probs[idx]) > best_prob:
                best_label = idx
                best_prob  = float(probs[idx])

        if best_label is not None:
            final_label  = best_label
            confidence   = float(probs[final_label])
            is_scam      = True
            is_uncertain = False
            print(f"[keyword override] label {pred_label} ({ID2LABEL.get(pred_label)}) "
                  f"→ {final_label} ({ID2LABEL.get(final_label)}) | prob={confidence:.3f}")
        else:
            is_uncertain = True
            print(f"[keyword override] không tìm được nhãn phù hợp → uncertain")
    else:
        is_uncertain = confidence < CONF_THRESHOLD

    # ── Tính top3 SAU khi final_label đã xác định → đồng nhất với chữ to ──
    top10_for_top3 = np.argsort(probs)[::-1][:10]
    filtered = [final_label]
    for idx in top10_for_top3:
        if int(idx) != final_label and len(filtered) < 3:
            filtered.append(int(idx))
    top3 = {ID2LABEL.get(i, str(i)): round(float(probs[i]), 4) for i in filtered}

    return {
        "label"       : final_label,
        "label_name"  : ID2LABEL.get(final_label, "Unknown"),
        "confidence"  : confidence,
        "is_scam"     : is_scam,
        "is_uncertain": is_uncertain,
        "scam_prob"   : scam_prob,
        "top3"        : top3,
    }

def gemini_explain(text: str, known_label: str = None, is_uncertain: bool = False) -> dict:
    if gemini_m is None:
        return _fallback_explain(known_label or "lua dao")

    if known_label and not is_uncertain:
        classify_block = f'Đây đã được xác định là "{known_label}". Không cần phân loại lại.'
        scam_type_val  = f'"{known_label}"'
    else:
        classify_block = (
            "Phân loại vào 1 trong các loại sau (hoặc đề xuất tên mới nếu không khớp):\n"
            + ", ".join(SCAM_CATEGORIES)
        )
        scam_type_val = '"Tên loại lừa đảo phù hợp nhất"'

    prompt = f"""Bạn là chuyên gia an ninh mạng phân tích lừa đảo tại Việt Nam.

Đoạn hội thoại sau có dấu hiệu lừa đảo.
{classify_block}

---
{text[:1500]}
---

Trả về JSON CHÍNH XÁC cấu trúc sau (không thêm markdown):
{{
  "scam_type": {scam_type_val},
  "summary": "Tóm tắt 1-2 câu",
  "why_dangerous": "Giải thích chiêu thức cụ thể",
  "steps": [
    {{"step": 1, "title": "Xác lập danh tính",          "desc": "..."}},
    {{"step": 2, "title": "Tạo áp lực/khẩn cấp",        "desc": "..."}},
    {{"step": 3, "title": "Thu thập thông tin nhạy cảm", "desc": "..."}},
    {{"step": 4, "title": "Yêu cầu hành động",           "desc": "..."}}
  ],
  "red_flags": ["Dấu hiệu 1", "Dấu hiệu 2", "Dấu hiệu 3"],
  "advice":    ["Lời khuyên 1", "Lời khuyên 2", "Lời khuyên 3"],
  "if_victim": "Việc cần làm ngay nếu đã bị lừa"
}}"""

    try:
        raw = re.sub(r"```json|```", "", gemini_m.generate_content(prompt).text).strip()
        return json.loads(raw)
    except Exception as e:
        print(f"[WARN] Gemini explain error: {e}")
        return _fallback_explain(known_label or "lua dao")

def gemini_chat(message: str, history: list) -> str:
    if gemini_m is None:
        return "Chatbot chưa được kích hoạt. Vui lòng cung cấp GEMINI_API_KEY."
    system = "Bạn là ScamShield AI - trợ lý chuyên về phòng chống lừa đảo tại Việt Nam. Trả lời bằng tiếng Việt, thân thiện, ngắn gọn và thực tế."
    chat_history = []
    for h in history[-6:]:
        chat_history.append({"role": "user",  "parts": [h["user"]]})
        chat_history.append({"role": "model", "parts": [h["bot"]]})
    try:
        return gemini_m.start_chat(history=chat_history).send_message(
            f"{system}\n\nCâu hỏi: {message}"
        ).text
    except Exception as e:
        return f"Xin lỗi, có lỗi xảy ra: {str(e)}"

def _fallback_explain(scam_type: str) -> dict:
    return {
        "scam_type"    : scam_type,
        "summary"      : f"Phát hiện dấu hiệu {scam_type}.",
        "why_dangerous": "Kẻ lừa đảo đang cố thu thập thông tin cá nhân hoặc yêu cầu chuyển tiền.",
        "steps": [
            {"step": 1, "title": "Xác lập danh tính",          "desc": "Giả mạo tổ chức/cá nhân uy tín"},
            {"step": 2, "title": "Tạo áp lực",                  "desc": "Tạo cảm giác khẩn cấp, sợ hãi"},
            {"step": 3, "title": "Thu thập thông tin nhạy cảm", "desc": "Yêu cầu CCCD, OTP, thông tin ngân hàng"},
            {"step": 4, "title": "Yêu cầu hành động",           "desc": "Chuyển tiền hoặc cài app độc hại"},
        ],
        "red_flags": ["Yêu cầu thông tin cá nhân", "Áp lực thời gian", "Đề nghị quá hấp dẫn"],
        "advice"   : ["Không cung cấp OTP", "Xác minh qua kênh chính thức", "Hỏi ý kiến người thân"],
        "if_victim": "Liên hệ ngân hàng ngay lập tức để khóa tài khoản. Báo cáo công an.",
    }


# FASTAPI APP

app = FastAPI(title="ScamShield AI", version="4.0")
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], allow_methods=["*"], allow_headers=["*"]
)

@app.on_event("startup")
async def startup():
    init_db()
    load_models()


# SCHEMAS

class RegisterRequest(BaseModel):
    username: str
    email: str
    password: str

class Turn(BaseModel):
    role: str
    content: str

class AnalyzeRequest(BaseModel):
    text    : Optional[str]        = None
    dialogue: Optional[List[Turn]] = None

class ChatRequest(BaseModel):
    message: str
    history: Optional[list] = []

class SaveReportRequest(BaseModel):
    is_scam    : bool
    risk_score : int
    confidence : float
    label_name : str
    input_text : Optional[str] = None
    explanation: Optional[dict] = None


# AUTH ENDPOINTS


@app.post("/auth/register", status_code=201)
def register(req: RegisterRequest):
    """Tạo tài khoản mới."""
    # Validate cơ bản
    if len(req.username.strip()) < 2:
        raise HTTPException(400, "Tên phải có ít nhất 2 ký tự.")
    if len(req.password) < 8:
        raise HTTPException(400, "Mật khẩu phải có ít nhất 8 ký tự.")
    if "@" not in req.email:
        raise HTTPException(400, "Email không hợp lệ.")

    hashed = hash_password(req.password)

    try:
        with db() as conn:
            cursor = conn.execute(
                "INSERT INTO users (username, email, hashed_pw) VALUES (?, ?, ?)",
                (req.username.strip(), req.email.lower().strip(), hashed)
            )
            user_id = cursor.lastrowid
    except sqlite3.IntegrityError:
        raise HTTPException(400, "Email đã được sử dụng. Vui lòng chọn email khác.")

    token = create_access_token(user_id, req.email.lower().strip())
    return {
        "access_token": token,
        "token_type"  : "bearer",
        "username"    : req.username.strip(),
        "email"       : req.email.lower().strip(),
    }


@app.post("/auth/login")
def login(form: OAuth2PasswordRequestForm = Depends()):
    """
    Đăng nhập — nhận form-data: username (= email), password.
    Trả JWT token.
    """
    email = form.username.lower().strip()

    with db() as conn:
        row = conn.execute(
            "SELECT id, username, email, hashed_pw FROM users WHERE email = ?", (email,)
        ).fetchone()

    if row is None or not verify_password(form.password, row["hashed_pw"]):
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Sai email hoặc mật khẩu.",
            headers={"WWW-Authenticate": "Bearer"},
        )

    token = create_access_token(row["id"], row["email"])
    return {
        "access_token": token,
        "token_type"  : "bearer",
        "username"    : row["username"],
        "email"       : row["email"],
    }


@app.get("/auth/me")
def me(current_user: dict = Depends(get_current_user)):
    """Trả thông tin user hiện tại từ token."""
    return current_user



# REPORT ENDPOINTS (cần đăng nhập)


@app.post("/save-report", status_code=201)
def save_report(
    req: SaveReportRequest,
    current_user: dict = Depends(get_current_user)
):
    """Lưu kết quả phân tích vào DB cho user đang đăng nhập."""
    explanation_str = json.dumps(req.explanation, ensure_ascii=False) if req.explanation else None

    with db() as conn:
        cursor = conn.execute(
            """INSERT INTO reports
               (user_id, is_scam, risk_score, confidence, label_name, input_text, explanation)
               VALUES (?, ?, ?, ?, ?, ?, ?)""",
            (
                current_user["id"],
                int(req.is_scam),
                req.risk_score,
                req.confidence,
                req.label_name,
                (req.input_text or "")[:500],    # giới hạn 500 chars
                explanation_str,
            )
        )
        report_id = cursor.lastrowid

    return {"ok": True, "report_id": report_id}


@app.get("/my-reports")
def my_reports(
    limit : int = 50,
    offset: int = 0,
    current_user: dict = Depends(get_current_user)
):
    """Lấy lịch sử phân tích của user (mới nhất trước)."""
    with db() as conn:
        rows = conn.execute(
            """SELECT id, is_scam, risk_score, confidence, label_name,
                      input_text, created_at
               FROM reports
               WHERE user_id = ?
               ORDER BY created_at DESC
               LIMIT ? OFFSET ?""",
            (current_user["id"], limit, offset)
        ).fetchall()

        total = conn.execute(
            "SELECT COUNT(*) FROM reports WHERE user_id = ?",
            (current_user["id"],)
        ).fetchone()[0]

    items = [dict(r) for r in rows]
    # Chuyển is_scam từ int về bool
    for item in items:
        item["is_scam"] = bool(item["is_scam"])

    return {"total": total, "items": items}


@app.delete("/my-reports/{report_id}")
def delete_report(
    report_id: int,
    current_user: dict = Depends(get_current_user)
):
    """Xóa 1 bản ghi phân tích (chỉ được xóa của chính mình)."""
    with db() as conn:
        row = conn.execute(
            "SELECT id, user_id FROM reports WHERE id = ?", (report_id,)
        ).fetchone()

        if row is None:
            raise HTTPException(404, "Không tìm thấy bản ghi.")
        if row["user_id"] != current_user["id"]:
            raise HTTPException(403, "Không có quyền xóa bản ghi này.")

        conn.execute("DELETE FROM reports WHERE id = ?", (report_id,))

    return {"ok": True}



# ANALYZE ENDPOINTS (giữ nguyên từ v3)


@app.get("/health")
def health():
    return {
        "status"    : "ok",
        "phobert"   : phobert is not None,
        "gemini"    : gemini_m is not None,
        "device"    : str(DEVICE),
        "num_labels": len(ID2LABEL),
        "threshold" : CONF_THRESHOLD,
    }


@app.post("/analyze")
async def analyze(req: AnalyzeRequest):
    if req.dialogue:
        text = dialogue_to_text([t.dict() for t in req.dialogue])
    elif req.text:
        text = normalize(req.text)
    else:
        raise HTTPException(400, "Cần cung cấp text hoặc dialogue")

    if len(text.strip()) < 10:
        raise HTTPException(400, "Nội dung quá ngắn")

    pred       = predict(text)
    risk_score = int(pred["scam_prob"] * 100)
    highlights = highlight_dangerous(text)

    explanation      = None
    final_label_name = pred["label_name"]
    top_labels       = pred["top3"]  # mặc định

    if pred["is_scam"] or pred["is_uncertain"]:
        explanation = gemini_explain(
            text,
            known_label  = None if pred["is_uncertain"] else pred["label_name"],
            is_uncertain = pred["is_uncertain"],
        )
        if explanation and pred["is_uncertain"]:
            final_label_name = explanation.get("scam_type", "Lừa đảo chưa phân loại")

            # Build lại top_labels với final_label_name lên đầu
            old_top = pred["top3"]
            top_labels = {final_label_name: old_top.get(final_label_name, max(old_top.values()))}
            for k, v in old_top.items():
                if k != final_label_name:
                    top_labels[k] = v

    return {
        "is_scam"     : pred["is_scam"] or pred["is_uncertain"],
        "is_uncertain": pred["is_uncertain"],
        "risk_score"  : risk_score,
        "label"       : pred["label"],
        "label_name"  : final_label_name,
        "confidence"  : round(pred["confidence"] * 100, 1),
        "top_labels"  : top_labels,   # ← dùng top_labels đã xử lý
        "highlights"  : highlights,
        "explanation" : explanation,
    }



@app.post("/analyze/realtime")
async def analyze_realtime(req: AnalyzeRequest):
    text_lower   = (req.text or "").lower()
    matched      = []
    danger_count = 0
    for pattern in SCAM_SIGNALS:
        if re.search(pattern, text_lower, re.IGNORECASE):
            danger_count += 1
            matched.append(pattern.split("|")[0])
    risk = min(danger_count * 25, 95)
    return {"risk_score": risk, "signals": matched[:3], "warning": risk > 40}


@app.post("/analyze/image")
async def analyze_image(file: UploadFile = File(...)):
    content_type = file.content_type or "image/jpeg"
    if not content_type.startswith("image/"):
        raise HTTPException(400, "Vui lòng upload file ảnh (JPG/PNG)")
    if gemini_m is None:
        raise HTTPException(500, "Gemini API chưa sẵn sàng")

    try:
        image_data = await file.read()
        image_b64 = base64.b64encode(image_data).decode("utf-8")

        ocr_prompt = """Trích xuất văn bản từ ảnh này.
Nếu là ảnh chụp màn hình tin nhắn (Zalo, Messenger, SMS):
- Tin nhắn bên TRÁI = Người lạ
- Tin nhắn bên PHẢI = Chủ máy
Sắp xếp theo thứ tự thời gian:
Người lạ: [nội dung]
Chủ máy: [nội dung]
Nếu là văn bản thường thì trích xuất bình thường.
Chỉ trả về văn bản, không giải thích."""

        extracted_text = gemini_m.generate_content([
            ocr_prompt,
            {"mime_type": content_type, "data": image_b64}  # ✅ dùng image_b64
        ]).text.strip()

        if len(extracted_text) < 5:
            raise HTTPException(400, "Không tìm thấy văn bản trong ảnh")

        pred             = predict(extracted_text)
        risk_score       = int(pred["scam_prob"] * 100)
        explanation      = None
        final_label_name = pred["label_name"]
        top_labels       = pred["top3"]  # mặc định

        if pred["is_scam"] or pred["is_uncertain"]:
            explanation = gemini_explain(
                extracted_text,
                known_label  = None if pred["is_uncertain"] else pred["label_name"],
                is_uncertain = pred["is_uncertain"],
            )
            if explanation and pred["is_uncertain"]:
                final_label_name = explanation.get("scam_type", "Lừa đảo chưa phân loại")

                # Build lại top_labels với final_label_name lên đầu
                old_top = pred["top3"]
                top_labels = {final_label_name: old_top.get(final_label_name, max(old_top.values()))}
                for k, v in old_top.items():
                    if k != final_label_name:
                        top_labels[k] = v

        return {
            "is_scam"       : pred["is_scam"] or pred["is_uncertain"],
            "is_uncertain"  : pred["is_uncertain"],
            "risk_score"    : risk_score,
            "label"         : pred["label"],
            "label_name"    : final_label_name,
            "confidence"    : round(pred["confidence"] * 100, 1),
            "top_labels"    : top_labels,  # ← đã sửa
            "highlights"    : [],
            "explanation"   : explanation,
            "extracted_text": extracted_text,
        }

    except HTTPException:
        raise
    except Exception as e:
        print(f"[ERROR] analyze_image: {e}")
        raise HTTPException(500, f"Lỗi khi đọc ảnh: {str(e)}")


@app.post("/chat")
async def chat(req: ChatRequest):
    if not req.message.strip():
        raise HTTPException(400, "Tin nhắn trống")
    return {"reply": gemini_chat(req.message, req.history or [])}


@app.get("/scam-types")
def get_scam_types():
    return {"types": [{"id": k, "name": v} for k, v in ID2LABEL.items() if k != 0]}