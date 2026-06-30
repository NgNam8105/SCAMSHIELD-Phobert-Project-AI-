CHƯƠNG 1. GIỚI THIỆU ĐỀ TÀI  
1.Giới thiệu đề tài  
Trong những năm gần đây, sự phát triển mạnh mẽ của các nền tảng nhắn tin, mạng xã hội và dịch vụ trực tuyến đã kéo theo sự gia tăng đáng kể của các hình thức lừa đảo qua tin nhắn tại Việt Nam. Theo phản ánh từ nhiều cơ quan chức năng và báo cáo an ninh mạng, số lượng tin nhắn, cuộc gọi và bài đăng có dấu hiệu lừa đảo ngày càng tăng cả về số lượng và mức độ tinh vi, với các chiêu thức phổ biến như giả mạo ngân hàng, giả danh cơ quan công quyền, lừa đặt phòng/đặt bàn, lừa tuyển dụng việc làm online, lừa đầu tư tài chính, lừa trúng thưởng, mạo danh người thân để vay tiền, và nhiều biến thể khác. Các đối tượng lừa đảo thường xuyên thay đổi cách hành văn, sử dụng từ viết tắt, chèn ký tự đặc biệt, viết sai chính tả có chủ đích để né tránh các bộ lọc dựa trên từ khóa truyền thống.  
Phần lớn người dùng, đặc biệt là người lớn tuổi hoặc ít tiếp xúc với công nghệ, gặp khó khăn trong việc nhận biết các dấu hiệu bất thường trong nội dung tin nhắn, dẫn đến nguy cơ bị chiếm đoạt tài sản hoặc thông tin cá nhân. Các giải pháp hiện có trên thị trường phần lớn dựa vào danh sách đen số điện thoại, đường dẫn (URL) hoặc bộ quy tắc từ khóa cố định, vốn có nhược điểm là dễ bị qua mặt khi nội dung tin nhắn được biến đổi linh hoạt, không khái quát hóa được cho các chiêu thức lừa đảo mới xuất hiện, và thường chỉ đưa ra kết quả phân loại nhị phân (lừa đảo / không lừa đảo) mà không cung cấp thông tin chi tiết về loại hình lừa đảo cụ thể hay mức độ nguy hiểm của tin nhắn.  
Xuất phát từ thực trạng trên, cùng với sự phát triển của các mô hình ngôn ngữ lớn được huấn luyện chuyên biệt cho tiếng Việt như PhoBERT, một mô hình biểu diễn ngôn ngữ dựa trên kiến trúc BERT được huấn luyện trên khối lượng lớn văn bản tiếng Việt, đề tài "Hệ thống phát hiện và đánh giá mức độ rủi ro tin nhắn lừa đảo bằng PhoBERT" được lựa chọn nhằm khai thác khả năng hiểu ngữ nghĩa sâu của mô hình ngôn ngữ hiện đại, kết hợp với các tín hiệu bổ trợ khác, để xây dựng một hệ thống có khả năng phát hiện, phân loại và đánh giá rủi ro của tin nhắn lừa đảo tiếng Việt một cách chính xác và linh hoạt hơn so với các phương pháp truyền thống.  
2. Mục tiêu của nghiên cứu  
Mục tiêu tổng quát của đề tài là xây dựng một hệ thống ứng dụng mô hình ngôn ngữ PhoBERT nhằm phát hiện tin nhắn có dấu hiệu lừa đảo bằng tiếng Việt, phân loại theo từng nhóm hình thức lừa đảo cụ thể, và đánh giá mức độ rủi ro tổng hợp của tin nhắn để hỗ trợ người dùng nhận diện và phòng tránh nguy cơ bị lừa đảo.  
Để đạt được mục tiêu tổng quát trên, đề tài đặt ra các mục tiêu cụ thể như sau:  
-	Xây dựng và huấn luyện mô hình phân loại nhị phân dựa trên PhoBERT để xác định một tin nhắn có khả năng là lừa đảo hay không, giải quyết vấn đề mất cân bằng dữ liệu giữa các nhãn trong quá trình huấn luyện.  
-	Xây dựng và huấn luyện mô hình phân loại đa lớp nhằm xác định loại hình lừa 
đảo cụ thể trong số nhiều nhóm hành vi lừa đảo phổ biến đã được khảo sát và gán 
nhãn, từ đó cung cấp thông tin chi tiết hơn cho người dùng về bản chất của tin nhắn đáng nghi.  
-	Xây dựng cơ chế tính điểm rủi ro (risk score) bằng cách kết hợp kết quả dự đoán 
từ mô hình AI với các tín hiệu phân tích metadata như số điện thoại, đường dẫn liên kết, từ khóa đặc trưng theo từng loại hình lừa đảo và các quy tắc cảnh báo bổ sung, nhằm đưa ra đánh giá tổng hợp toàn diện hơn so với việc chỉ dựa vào một nguồn thông tin duy nhất.  
-	Thiết kế và triển khai hệ thống ở dạng ứng dụng web hoàn chỉnh, bao gồm phần 
backend xử lý mô hình và logic nghiệp vụ, cùng phần giao diện người dùng cho phép nhập tin nhắn, đoạn hội thoại cần kiểm tra và hiển thị kết quả phân tích một cách trực quan, dễ hiểu.  
3. Đối tượng và phạm vi nghiên cứu  
Đối tượng nghiên cứu của đề tài là các tin nhắn văn bản tiếng Việt có nội dung liên quan đến hành vi lừa đảo, bao gồm tin nhắn SMS, tin nhắn trên các ứng dụng chat, email ngắn và các nội dung tương tự, được thu thập, tổng hợp và bổ sung thông qua các kỹ thuật tăng cường dữ liệu để đảm bảo tính đa dạng và cân bằng giữa các nhóm hành vi lừa đảo.  
Phạm vi nghiên cứu của đề tài tập trung vào việc xử lý ngôn ngữ tự nhiên tiếng Việt, sử dụng mô hình nền PhoBERT làm cơ sở cho các bài toán phân loại văn bản. Hệ thống được xây dựng để xử lý nội dung dạng văn bản; các nội dung dạng khác như hình ảnh có thể được hỗ trợ phân tích bổ trợ thông qua các dịch vụ AI bên ngoài nhưng không phải là trọng tâm chính của mô hình huấn luyện. Đề tài không đi sâu vào việc xử lý các cuộc gọi thoại trực tiếp hoặc các nội dung video, và không thực hiện các biện pháp can thiệp pháp lý hay kỹ thuật nhằm chặn, xử lý đối tượng lừa đảo, mà chỉ tập trung vào khía cạnh phát hiện, phân loại và cảnh báo rủi ro cho người dùng.  
4.Phương pháp nghiên cứu  
Đề tài kết hợp nhiều phương pháp nghiên cứu để giải quyết các mục tiêu đã đặt ra. Về phương pháp lý thuyết, đề tài tiến hành nghiên cứu và tổng hợp các tài liệu liên quan đến xử lý ngôn ngữ tự nhiên, mô hình biểu diễn ngôn ngữ dựa trên kiến trúc Transformer, đặc biệt là PhoBERT, cùng các nghiên cứu về phát hiện gian lận, lừa đảo và phân loại văn bản tiếng Việt.  
Về phương pháp thực nghiệm, đề tài tiến hành xây dựng tập dữ liệu huấn luyện gồm các tin nhắn lừa đảo và không lừa đảo, được gán nhãn theo hai cấp độ: nhãn nhị phân (lừa đảo/không lừa đảo) và nhãn đa lớp (loại hình lừa đảo cụ thể). Dữ liệu được làm sạch, chuẩn hóa và tăng cường bằng các kỹ thuật sinh dữ liệu tổng hợp nhằm cải thiện độ cân bằng giữa các nhóm nhãn, đặc biệt đối với các loại hình lừa đảo có số lượng mẫu ít. Mô hình PhoBERT được finetune trên tập dữ liệu này theo phương pháp học có giám sát. Đề tài đã thử nghiệm hai hướng tiếp cận kiến trúc: single-head 30 nhãn (một lớp phân loại duy nhất cho cả 30 nhãn) và multitask 2-head (hai lớp phân loại riêng biệt cho bài toán nhị phân và đa lớp). Sau khi so sánh, phương án single-head (single-head multi-class) được lựa chọn làm kiến trúc chính thức của hệ thống nhờ tính nhất quán đầu ra và quy trình huấn luyện đơn giản hơn. 
Về phương pháp xây dựng hệ thống, đề tài áp dụng phương pháp phát triển phần mềm theo hướng module hóa, trong đó phần backend được xây dựng bằng FastAPI để cung cấp các API xử lý dự đoán, kết hợp với một bộ quy tắc đánh giá rủi ro dựa trên metadata được thiết kế song song với mô hình AI. Phần giao diện người dùng được xây dựng dưới dạng ứng dụng web nhằm đảm bảo khả năng triển khai và sử dụng thuận tiện.  
 
CHƯƠNG 2: CƠ SỞ LÝ THUYẾT VÀ CÔNG NGHỆ LIÊN QUAN  
2.1. Tổng quan về Trí tuệ nhân tạo và Học máy  
Trí tuệ nhân tạo (Artificial Intelligence - AI) là lĩnh vực khoa học máy tính nghiên cứu cách xây dựng các hệ thống có khả năng thực hiện những nhiệm vụ đòi hỏi trí tuệ con người, như suy luận, nhận diện mẫu, ra quyết định và xử lý ngôn ngữ.  
Học máy (Machine Learning - ML) là một nhánh của AI, trong đó hệ thống không được lập trình tường minh từng quy tắc xử lý, mà tự học các quy luật từ dữ liệu thông qua quá trình huấn luyện. Các bài toán học máy thường được chia thành ba nhóm chính:  
   
hình 1:AI và ML  
●	Học có giám sát (Supervised Learning): Mô hình học từ dữ liệu đã được gán nhãn để dự đoán nhãn cho dữ liệu mới.  
●	Học không giám sát (Unsupervised Learning): Hệ thống tìm kiếm và phát hiện cấu trúc ẩn trong dữ liệu không có nhãn.  
●	Học tăng cường (Reinforcement Learning): Mô hình học thông qua tương tác với môi trường và tối ưu hóa phần thưởng nhận được.  
Ứng dụng trong đề tài: Bài toán phát hiện và phân loại tin nhắn lừa đảo trong đề tài này thuộc nhóm học có giám sát, cụ thể là bài toán phân loại văn bản (text classification). Mô hình được huấn luyện trên tập dữ liệu tin nhắn đã được gán nhãn loại hình lừa đảo để từ đó dự đoán nhãn cho các tin nhắn mới.  
2.2. Học sâu (Deep Learning)  
Khái niệm và đặc điểm cốt lõi  
●	Cấu trúc mạng nơ-ron: Học sâu là phương pháp học máy dựa trên các mạng nơ-ron nhân tạo (Artificial Neural Network) gồm nhiều lớp xếp chồng lên nhau. Mỗi lớp sẽ học cách biến đổi dữ liệu đầu vào thành các biểu diễn trừu tượng hơn ở lớp tiếp theo.  
●	Tự động học đặc trưng: Khác với các phương pháp học máy truyền thống nơi đặc trưng (feature) thường phải được thiết kế thủ công bởi con người, học sâu có khả năng tự học các đặc trưng trực tiếp từ dữ liệu thô thông qua quá trình huấn luyện. Điều này giúp giảm thiểu sự phụ thuộc vào tri thức chuyên gia và cải thiện đáng kể hiệu quả trên các bài toán có dữ liệu phức tạp, nhiều chiều.  
   
Hình 2: Mối quan hệ giữa AI, ML , DL  
Động lực phát triển Sự phát triển vượt bậc của học sâu gắn liền với ba yếu tố bản lề: sự gia tăng về khối lượng dữ liệu, sự nâng cấp về sức mạnh tính toán (đặc biệt là GPU), và các thuật toán huấn luyện hiệu quả như lan truyền ngược (backpropagation). Nhờ những yếu tố này, học sâu đã và đang làm thay đổi nhiều lĩnh vực, từ nhận diện hình ảnh, giọng nói đến xử lý ngôn ngữ tự nhiên.  
Các kiến trúc học sâu phổ biến  
●	Mạng nơ-ron tích chập (CNN): Thường được sử dụng cho dữ liệu dạng ảnh nhờ khả năng trích xuất các đặc trưng không gian cục bộ một cách tối ưu.  
●	Mạng nơ-ron hồi quy (RNN) và các biến thể (LSTM, GRU): Rất hiệu quả cho dữ liệu dạng chuỗi như văn bản, âm thanh do khả năng xử lý và ghi nhớ thông tin theo trình tự thời gian.  
●	Kiến trúc Transformer: Mặc dù ra đời sau, kiến trúc này hiện là nền tảng cốt lõi cho hầu hết các mô hình ngôn ngữ hiện đại. Transformer vượt trội hơn RNN nhờ cơ chế 
tự chú ý (self-attention), cho phép xử lý dữ liệu song song và nắm bắt ngữ cảnh toàn cục một cách toàn diện hơn.  
Ứng dụng trong đề tài Trong phạm vi đề tài này, kiến trúc Transformer – cụ thể là mô hình ngôn ngữ PhoBERT – được lựa chọn làm công nghệ nền tảng để giải quyết bài toán phát hiện và phân loại tin nhắn lừa đảo tiếng Việt. Chi tiết về kiến trúc và mô hình này sẽ được trình bày cụ thể ở các phần sau.  
  
2.3. Tổng quan về xử lý ngôn ngữ tự nhiên  
2.3.1. Khái niệm và mục tiêu  
●	Xử lý ngôn ngữ tự nhiên (Natural Language Processing - NLP) là một lĩnh vực thuộc trí tuệ nhân tạo, tập trung vào việc giúp máy tính có khả năng hiểu, phân tích và xử lý ngôn ngữ của con người dưới dạng văn bản hoặc giọng nói.  
●	Mục tiêu: Thu hẹp khoảng cách giữa ngôn ngữ tự nhiên (vốn có cấu trúc linh hoạt, nhiều tầng ý nghĩa và phụ thuộc bối cảnh) với ngôn ngữ máy tính, từ đó cho phép máy tính thực hiện các tác vụ liên quan đến ngôn ngữ một cách tự động.  
   
Hình 3: NLP  
2.3.2. Các bài toán NLP phổ biến và ứng dụng trong đề tài  
Một số bài toán phổ biến trong lĩnh vực NLP bao gồm: nhận diện thực thể có tên (Named Entity Recognition), phân tích cảm xúc (Sentiment Analysis), dịch máy (Machine Translation), tóm tắt văn bản, và phân loại văn bản (Text Classification).  
Bài toán cốt lõi của đề tài: Đề tài tập trung vào bài toán phân loại văn bản. Từ một đoạn văn bản đầu vào (tin nhắn), hệ thống cần xác định văn bản đó thuộc nhóm nhãn nào trong tập các nhãn đã được định nghĩa trước. Cụ thể:  
1.	Xác định tin nhắn có phải là lừa đảo hay không.  
2.	Nếu là lừa đảo, phân loại chi tiết xem tin nhắn đó thuộc loại hình nào.  
2.3.3. Các thách thức đặc thù khi xử lý tiếng Việt  
Đối với tiếng Việt, quá trình NLP gặp phải một số thách thức đặc thù so với các ngôn ngữ như tiếng Anh:  
●	Vấn đề tách từ (Word Segmentation): Tiếng Việt là ngôn ngữ đơn lập, không có khoảng trắng phân tách rõ ràng giữa các từ ghép. Một từ có thể gồm nhiều âm tiết được viết cách nhau bởi khoảng trắng nhưng vẫn mang một ý nghĩa duy nhất (ví dụ: "ngân hàng", "đặt bàn").  
●	Hệ thống dấu thanh phong phú: Việc bỏ dấu hoặc viết sai dấu có thể làm thay đổi hoàn toàn ý nghĩa của câu. Đây cũng là thủ đoạn rất phổ biến trong các tin nhắn lừa đảo nhằm mục đích né tránh các bộ lọc từ khóa truyền thống.  
●	Ngôn ngữ mạng và các biến thể: Ngôn ngữ trong tin nhắn thực tế thường thiếu chuẩn mực, chứa nhiều từ viết tắt, teencode, ký tự đặc biệt hoặc các lỗi chính tả cố ý.  
  
2.4. Kiến trúc Transformer và mô hình BERT/PhoBERT  
2.4.1. Mô hình ngôn ngữ và Kiến trúc Transformer  
●	Mô hình ngôn ngữ (Language Model): Là mô hình thống kê hoặc học máy có khả năng học phân bố xác suất của các chuỗi từ, từ đó hiểu được mối quan hệ ngữ nghĩa và ngữ pháp. Thay vì biểu diễn từ dưới dạng vector rời rạc, các mô hình hiện đại học các vector biểu diễn (embedding) mang thông tin ngữ nghĩa sâu sắc, giúp các từ có ý nghĩa gần nhau sẽ nằm gần nhau trong không gian vector.  
●	Sự đột phá của kiến trúc Transformer: Ra đời từ bài báo "Attention Is All You Need" (Vaswani và cộng sự, 2017), Transformer đã khắc phục hoàn toàn những hạn chế của kiến trúc hồi quy tuần tự (RNN, LSTM) trước đó.  
●	Cơ chế tự chú ý (Self-attention): Đây là cốt lõi của Transformer, cho phép mô hình tính toán đồng thời mức độ liên quan giữa mỗi từ với tất cả các từ khác trong câu. Khác với việc xử lý từng từ một của RNN, cơ chế này giúp nắm bắt các mối liên hệ phụ thuộc xa một cách toàn diện và tối ưu hóa hiệu năng huấn luyện song song trên phần cứng hiện đại.  
   
𝑄𝐾𝑇
𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑄, 𝐾, 𝑉) = 𝑠𝑜𝑓𝑡𝑚𝑎𝑥   𝑉 √𝑑𝑘 Trong đó: 
●	Q (Query): Ma trận biểu diễn truy vấn, được tạo từ đầu vào của mô hình và dùng để xác định thông tin cần tìm kiếm.  
●	K (Key): Ma trận khóa, biểu diễn đặc trưng của các phần tử đầu vào để so khớp với Query.  
●	V (Value): Ma trận giá trị, chứa thông tin sẽ được tổng hợp và truyền sang bước tiếp theo dựa trên trọng số attention.  
●	𝑑𝑘: Kích thước (số chiều) của vector Key 
 
  
 
2.4.2. Học chuyển giao (Transfer Learning)  
Gắn liền với kiến trúc Transformer là phương pháp học chuyển giao theo hướng Tiền huấn luyện và Tinh chỉnh (Pre-training - Fine-tuning):  
●	Tiền huấn luyện (Pre-training): Mô hình được huấn luyện trên một lượng văn bản khổng lồ qua các tác vụ tự giám sát (self-supervised) để tích lũy biểu diễn ngôn ngữ tổng quát.  
●	Tinh chỉnh (Fine-tuning): Mô hình sau đó được huấn luyện tiếp trên một tập dữ liệu nhỏ hơn, gắn với bài toán cụ thể.  
●	Ưu điểm: Cách tiếp cận này giúp tận dụng tối đa tri thức đã học, giảm đáng kể lượng dữ liệu và thời gian huấn luyện cho các bài toán chuyên biệt, đồng thời mang lại hiệu năng vượt trội so với việc xây dựng mô hình từ đầu.  
2.4.3. Mô hình BERT  
Dựa trên nền tảng Transformer, Google đã giới thiệu mô hình BERT (Bidirectional Encoder Representations from Transformers) vào năm 2018. 
●	Đặc trưng hai chiều (Bidirectional): Sử dụng phần encoder của Transformer, BERT có khả năng khai thác thông tin từ cả phía trước và phía sau của một từ khi xử lý, giúp nắm bắt ngữ cảnh trọn vẹn hơn.  
●	Các tác vụ tiền huấn luyện: BERT được huấn luyện thông qua hai tác vụ tự giám sát chính:  
○ Mô hình hóa ngôn ngữ có che (Masked Language Model - MLM): Dự đoán các từ bị ẩn đi ngẫu nhiên dựa vào ngữ cảnh xung quanh.  
○ Dự đoán câu tiếp theo (Next Sentence Prediction - NSP): Giúp học mối quan hệ logic giữa hai câu liên tiếp.  
   
Hình 4 : tổng quan về bert  
2.4.4. Mô hình PhoBERT và ứng dụng trong đề tài  
●	Hạn chế của BERT đa ngôn ngữ: Các phiên bản multilingual BERT thường không tối ưu cho tiếng Việt do dữ liệu huấn luyện ít và bộ tách từ (tokenizer) không được thiết kế riêng.  
●	Sự ra đời của PhoBERT: Để khắc phục, VinAI đã giới thiệu PhoBERT (2020) dựa trên kiến trúc BERT/RoBERTa. Mô hình này được huấn luyện hoàn toàn trên dữ liệu tiếng Việt khối lượng lớn cùng bộ tách từ chuyên biệt (giúp xử lý tốt từ ghép và ngữ pháp). Nhờ vậy, PhoBERT đạt hiệu quả vượt trội trên các tác vụ phân loại, phân tích cảm xúc và nhận diện thực thể tiếng Việt.  
●	Kiến trúc PhoBERT (phiên bản base): Gồm nhiều lớp encoder của Transformer xếp chồng lên nhau. Mỗi lớp sử dụng cơ chế tự chú ý đa đầu (multi-head selfattention) và mạng truyền thẳng (feed-forward network) để học biểu diễn ngữ nghĩa đa chiều.  
  
Hình 4b: Cấu trúc chi tiết một Encoder Layer trong PhoBER 
Như thể hiện trong Hình 4b, mỗi Encoder Layer gồm hai khối biến đổi chính — MultiHead Self-Attention và Feed-Forward Network — mỗi khối đều được theo sau bởi một phép cộng dư (residual connection) và chuẩn hóa lớp (Layer Normalization): 
𝐻 = 𝐿𝑎𝑦𝑒𝑟𝑁𝑜𝑟𝑚(𝑋 + 𝑀𝑢𝑙𝑡𝑖𝐻𝑒𝑎𝑑𝐴𝑡𝑡𝑒𝑛𝑡𝑖𝑜𝑛(𝑋)) 
𝑌 = LayerNorm(𝐻 + FFN(𝐻)) 
Residual connection giúp gradient có một đường truyền tắt (shortcut) để lan truyền ngược qua nhiều lớp mà không bị suy giảm dần (vanishing gradient) — yếu tố then chốt cho phép Transformer xếp chồng tới 12 lớp encoder mà vẫn huấn luyện ổn định. PhoBERT-base-v2 lặp lại cấu trúc Encoder Layer này 12 lần liên tiếp để tạo thành toàn bộ mô hình nền. Cách thức 6 lớp đầu được đóng băng và 6 lớp sau được tinh chỉnh riêng cho bài toán ScamShield sẽ được trình bày chi tiết tại mục 3.5. 
● Ứng dụng thực tiễn trong hệ thống: Đề tài lựa chọn phiên bản vinai/phobert-basev2 làm mô hình nền (backbone). Bằng cách bổ sung một lớp phân loại đa lớp 
(classification head) và tinh chỉnh trên tập dữ liệu tin nhắn lừa đảo tiếng Việt đã được gán nhãn, hệ thống giải quyết bài toán phân loại văn bản đa lớp, qua đó vừa phát hiện tin nhắn có dấu hiệu lừa đảo hay không, vừa xác định loại hình lừa đảo cụ thể trong cùng một lần dự đoán. Chi tiết về thiết kế bài toán và kiến trúc phân loại được trình bày tại phần 2.5   
2.5. Bài toán phân loại văn bản đa lớp với PhoBERT   
Định dạng bài toán và cấu trúc tập nhãn  
●	Phân loại đa lớp (Multi-class Text Classification): Trong đề tài này, bài toán phát hiện và phân loại tin nhắn lừa đảo được hợp nhất và thiết kế dưới dạng một bài toán phân loại đa lớp duy nhất thay vì chia thành nhiều bước rời rạc.  
●	Tập nhãn (30 nhãn): * Nhãn 0: Đại diện cho tin nhắn an toàn, "Không phải lừa đảo".  
○ Nhãn 1 đến 29: Tương ứng với từng loại hình lừa đảo cụ thể (ví dụ: giả mạo công an, giả mạo ngân hàng, lừa đảo đặt phòng/đặt bàn, lừa đảo đầu tư,...).  
●	Logic suy luận: Việc xác định tính chất lừa đảo của tin nhắn được suy ra trực tiếp từ kết quả phân loại. Nếu mô hình dự đoán nhãn khác 0, hệ thống tự động đánh giá đây là tin nhắn có dấu hiệu lừa đảo, đồng thời nhãn dự đoán sẽ chỉ ra chính xác loại hình tương ứng.  
Kiến trúc phân loại  
●	Mô hình nền (Backbone): PhoBERT được sử dụng làm bộ trích xuất đặc trưng để lấy ra các biểu diễn ngữ nghĩa sâu của văn bản đầu vào.  
●	Lớp phân loại (Classification Head): Biểu diễn đầu ra từ PhoBERT được đưa qua một lớp phân loại duy nhất với số lượng đầu ra tương ứng với kích thước tập nhãn (30 đầu ra).  
●	Hàm kích hoạt: Hàm Softmax được áp dụng ở lớp cuối cùng để tính toán phân bố xác suất trên tất cả các nhãn.  
  
𝑒𝑧𝑘
	𝑃(𝑦 = 𝑘 ∣ 𝑥) =  𝑒𝑧𝑗 , 	𝑘 ∈ {0,1, … ,29} 
Trong đó 
 −𝑃(𝑦 = 𝑘 ∣ 𝑥) : Xác suất mô hình dự đoán mẫu đầu vào 𝑥thuộc nhãn 𝑘.  
  -𝑥: Văn bản đầu vào sau khi đã được tiền xử lý và tokenize.  
  −𝑦: Nhãn dự đoán của mô hình đối với mẫu đầu vào 𝑥.  
  −𝑘: Chỉ số của nhãn cần tính xác suất. Trong đề tài này, 𝑘 ∈ {0,1, … ,29}, tương ứng với 30 loại tin nhắn lừa đảo.  
  −𝑧𝑘: Giá trị logit của nhãn 𝑘được tạo ra từ classification head trước khi áp dụng hàm Softmax.  
  −𝑧𝑗: Giá trị logit của nhãn thứ 𝑗, với 𝑗 = 0,1, … ,29.  
  −𝑒: Hằng số Euler, có giá trị xấp xỉ 2,71828.  
    𝑒𝑧𝑗: Tổng các giá trị mũ của toàn bộ 30 logit, đóng vai trò chuẩn hóa để tổng xác suất của tất cả các nhãn bằng 1. 
 
●	Ưu điểm của thiết kế: Việc sử dụng một mô hình với một head duy nhất không chỉ đơn giản hóa quá trình huấn luyện và triển khai, mà còn đảm bảo tính nhất quán tự nhiên. Vì cả kết quả "tồn tại lừa đảo" và "loại hình lừa đảo" đều xuất phát từ cùng một nhãn dự đoán, hệ thống tránh được hoàn toàn rủi ro mâu thuẫn đầu ra (ví dụ: mô hình 1 báo có lừa đảo nhưng mô hình 2 lại không phân loại được loại hình) như khi sử dụng các mô hình rời rạc.  
Khai thác phân bố xác suất đầu ra Bên cạnh kết quả phân loại trực tiếp (nhãn có xác suất cao nhất), hệ thống còn tận dụng phân bố xác suất trên toàn bộ 30 nhãn thu được từ hàm Softmax để thực hiện các chức năng đánh giá chuyên sâu:  
●	Tính toán điểm rủi ro (Risk Score): Đánh giá mức độ nguy hiểm tổng thể của đoạn tin nhắn dựa trên việc tổng hợp xác suất của tất cả các nhãn thuộc nhóm lừa đảo.  
●	Đánh giá độ chắc chắn (Confidence Threshold): Dựa vào mức xác suất cao nhất dự đoán được, hệ thống đo lường độ tin cậy của mô hình. Từ ngưỡng tin cậy này, hệ thống sẽ quyết định việc kích hoạt các cơ chế hỗ trợ bổ sung ra quyết định (như ghi đè nhãn bằng từ khóa - keyword override, hay sinh giải thích bằng LLM), sẽ được trình bày chi tiết tại phần 2.8.  
2.6. Các vấn đề kỹ thuật trong huấn luyện mô hình  
Trong quá trình tinh chỉnh và huấn luyện mô hình, một số vấn đề kỹ thuật đặc thù đối với dữ liệu văn bản thực tế đã được đặt ra và giải quyết bằng các chiến lược cụ thể như sau:  
●	Xử lý mất cân bằng dữ liệu (Class Imbalance):  
0	Vấn đề: Số lượng mẫu dữ liệu thu thập được giữa các loại hình lừa đảo có sự chênh lệch lớn, dễ dẫn đến hiện tượng mô hình "học lệch", ưu tiên dự đoán các nhãn chiếm đa số và bỏ qua các nhãn thiểu số.  
○ Giải pháp: Áp dụng kỹ thuật lấy mẫu có trọng số (Weighted Random Sampling), trong đó mỗi mẫu dữ liệu được gán một trọng số lấy mẫu tỉ lệ nghịch với số lượng mẫu của nhãn tương ứng (1/số_mẫu_của_nhãn). Trong mỗi epoch huấn luyện, các mẫu thuộc nhãn thiểu số sẽ được lấy ra   
○ (oversample) với tần suất cao hơn so với phân bố gốc, giúp mô hình được tiếp xúc cân bằng hơn giữa các loại hình lừa đảo, kể cả các loại có ít dữ liệu thu thập được.  
●	Tăng cường dữ liệu (Data Augmentation):  
0	Mục tiêu: Mở rộng và làm phong phú tập huấn luyện, đặc biệt là đối với các nhóm nhãn đang bị thiếu hụt dữ liệu.  
1
𝑤𝑖 =   
|{𝑗: 𝑦𝑗 = 𝑦𝑖}|              Trong đó: 
 𝑤𝑖: Trọng số của mẫu thứ 𝑖, được sử dụng trong quá trình huấn luyện để điều chỉnh mức độ đóng góp của mẫu đó vào hàm mất mát.  
𝑦𝑖: Nhãn thật của mẫu thứ 𝑖.  
𝑦𝑗: Nhãn của mẫu thứ 𝑗trong tập dữ liệu.  
{𝑗: 𝑦𝑗 = 𝑦𝑖}: Tập hợp tất cả các chỉ số 𝑗sao cho mẫu thứ 𝑗có cùng nhãn với mẫu thứ 𝑖.  ∣ {𝑗: 𝑦𝑗 = 𝑦𝑖} ∣: Số lượng mẫu thuộc cùng nhãn với mẫu thứ 𝑖, hay chính là tần suất xuất hiện của nhãn đó trong tập dữ liệu.  
 
○ Phương pháp: Sinh thêm các mẫu văn bản, đoạn hội thoại hoặc tin nhắn mới tương tự như dữ liệu gốc. Kỹ thuật này không chỉ giúp cân bằng lại phân bố các lớp mà còn tăng tính đa dạng cho dữ liệu, giúp mô hình tổng quát hóa (generalize) tốt hơn trong thực tế.  
●	Xử lý giới hạn độ dài đầu vào (Input Length Limit):  
0	Vấn đề: Do bản chất của kiến trúc Transformer, mô hình PhoBERT có giới hạn cố định về độ dài chuỗi token đầu vào (max_length). Tuy nhiên, nhiều mẫu dữ liệu ở dạng hội thoại nhiều lượt có tổng độ dài vượt quá giới hạn này.  ○ Giải pháp: Đối với các mẫu dữ liệu dạng hội thoại nhiều lượt, hệ thống chỉ giữ lại 8 lượt trao đổi cuối cùng trước khi ghép thành văn bản đầu vào, vì các thông tin mang tính quyết định (red flags) như yêu cầu chuyển khoản, cung cấp mã OTP, truy cập đường link... thường xuất hiện ở giai đoạn cuối của cuộc trò chuyện lừa đảo. Văn bản sau khi ghép được đưa vào PhoBERT với giới hạn độ dài chuỗi token là 256 (max_length=256), áp dụng cơ chế cắt và đệm (truncation/padding) chuẩn của tokenizer.  
●	Kiểm soát quá trình huấn luyện (Training Control):  
0	Kỹ thuật: Sử dụng cơ chế dừng sớm (Early Stopping) để kiểm soát vòng lặp huấn luyện.  
○ Tác dụng: Hệ thống sẽ liên tục theo dõi hiệu năng của mô hình trên tập kiểm định (validation set). Nếu các chỉ số đánh giá không có sự cải thiện qua một số lượng epoch nhất định (patience), quá trình huấn luyện sẽ tự động dừng lại nhằm ngăn chặn tình trạng học vẹt (overfitting).  
●	Lựa chọn độ đo đánh giá phù hợp (Model Evaluation):  
0	Vấn đề: Trong điều kiện tập dữ liệu bị mất cân bằng trầm trọng, nếu chỉ sử dụng độ chính xác tổng thể (Accuracy) sẽ gây ra những nhận định sai lệch về năng lực thực sự của mô hình (đạt điểm cao chỉ nhờ đoán đúng lớp đa số).  ○ Giải pháp: Áp dụng kết hợp Accuracy với các độ đo chuyên sâu hơn bao gồm Precision (Độ chính xác), Recall (Độ phủ) và F1-score (theo trung bình macro). Việc đánh giá đa chiều giúp đo lường chính xác hiệu suất nhận diện của mô hình trên từng loại hình lừa đảo riêng biệt, kể cả các lớp thiểu số.  
2.7. Các độ đo đánh giá hiệu năng mô hình phân loại  
Ma trận nhầm lẫn (Confusion Matrix) Đây là công cụ cơ sở để đánh giá hiệu quả của một hệ thống phân loại, thể hiện chi tiết số lượng dự đoán đúng và sai của mô hình theo từng lớp dưới dạng bảng ma trận:  
●	Đường chéo chính: Biểu diễn số lượng các mẫu được mô hình dự đoán hoàn toàn chính xác.  
●	Các phần tử ngoài đường chéo: Biểu diễn các trường hợp sai lệch, cho biết mô hình đang nhầm lẫn giữa những lớp cụ thể nào với nhau.  
Các độ đo định lượng Từ ma trận nhầm lẫn, các chỉ số đánh giá cốt lõi được tính toán để đo lường chất lượng mô hình:  
●	Độ chính xác tổng thể (Accuracy): Tỷ lệ tổng số dự đoán đúng trên tổng số mẫu. Tuy nhiên, độ đo này không phản ánh đúng thực tế và có thể gây hiểu nhầm lớn khi áp dụng trên tập dữ liệu mất cân bằng.   
	∑29𝑘=0	𝑇𝑃𝑘
𝐴𝑐𝑐𝑢𝑟𝑎𝑐𝑦 =   
𝑁 Trong đó: 
     -Accuracy: Độ chính xác tổng thể của mô hình, thể hiện tỷ lệ mẫu được phân loại đúng trên tổng số mẫu kiểm định.  
 𝑇𝑃𝑘(True Positive): Số mẫu thực sự thuộc nhãn 𝑘và được mô hình dự đoán đúng là nhãn 𝑘.  
	  ∑29𝑘=0	𝑇𝑃𝑘: Tổng số mẫu được dự đoán chính xác trên toàn bộ 30 nhãn của bài toán phân loại.  
  𝑁: Tổng số mẫu trong tập kiểm định (test set) được sử dụng để đánh giá mô hình.  
  𝑘 ∈ {0,1, … ,29}: Chỉ số của các nhãn trong bài toán phân loại đa lớp gồm 30 loại tin nhắn lừa đảo. 
  
●	Độ chính xác (Precision): Tỷ lệ dự đoán đúng trên tổng số các mẫu được mô hình dự đoán thuộc một lớp cụ thể. Chỉ số này phản ánh độ tin cậy của các dự đoán dương (hạn chế báo động giả).   
𝑇𝑃𝑘
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑘 =   
𝑇𝑃𝑘 + 𝐹𝑃𝑘
• TPₖ (True Positive): Số mẫu thực sự thuộc nhãn k và được mô hình dự đoán đúng là nhãn k. • FPₖ (False Positive): Số mẫu không thuộc nhãn k nhưng bị mô hình dự đoán nhầm thành nhãn k. 
Ý nghĩa thực tiễn: Precision cao đồng nghĩa với việc mô hình có ít dự đoán dương tính giả (false positive). Nói cách khác, khi mô hình kết luận một tin nhắn thuộc loại lừa đảo k, thì khả năng cao dự đoán đó là chính xác. 
●	Độ phủ (Recall): Tỷ lệ mô hình phát hiện đúng trên tổng số các mẫu thực sự thuộc về lớp đó. Chỉ số này phản ánh khả năng "không bỏ sót" của hệ thống.  
  
𝑇𝑃𝑘
𝑅𝑒𝑐𝑎𝑙𝑙𝑘 =   
𝑇𝑃𝑘 + 𝐹𝑁𝑘
  Recallₖ: Độ bao phủ (Recall) của nhãn 𝑘, thể hiện khả năng mô hình phát hiện đúng các mẫu thuộc nhãn 𝑘.  
  TPₖ (True Positive): Số mẫu thực sự thuộc nhãn 𝑘và được mô hình dự đoán đúng là nhãn 𝑘.  
  FNₖ (False Negative): Số mẫu thực sự thuộc nhãn 𝑘nhưng bị mô hình dự đoán nhầm sang các nhãn khác.  
●	F1-score: Là trung bình điều hòa giữa Precision và Recall, được dùng làm thước đo tổng hợp khi cần cân bằng giữa việc không nhận diện sai và không bỏ sót.   
2 × 𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑘 × 𝑅𝑒𝑐𝑎𝑙𝑙𝑘
𝐹1𝑘 =   
𝑃𝑟𝑒𝑐𝑖𝑠𝑖𝑜𝑛𝑘 + 𝑅𝑒𝑐𝑎𝑙𝑙𝑘
Trung bình điều hòa giữa Precision và Recall, bằng 1 khi cả hai đều hoàn hảo, bằng 0 khi một trong hai bằng 0   
●	Macro-F1 (Trung bình Macro): Đối với bài toán phân loại đa lớp có dữ liệu mất cân bằng trầm trọng như trong đề tài, F1-score tính theo trung bình macro được ưu tiên sử dụng. Bằng cách tính trung bình cộng F1-score của tất cả các lớp (không màng đến số lượng mẫu của lớp đó), Macro-F1 đảm bảo các nhãn thiểu số cũng được đánh giá công bằng, tránh tình trạng điểm số bị chi phối hoàn toàn bởi các lớp đa số.  
  
	𝑀𝑎𝑐𝑟𝑜  	𝐹1𝑘 
𝑘=0 Trong đó: 
●	Macro-F1: Điểm F1 trung bình của toàn bộ các lớp.  
●	𝐹1𝑘: Điểm F1 của lớp thứ 𝑘.  
●	𝑘: Chỉ số lớp (class index).  
●	∑29𝑘=0	: Tổng điểm F1 của tất cả 30 lớp, từ lớp 0 đến lớp 29.  
●	30: Tổng số lớp trong bài toán phân loại.  
●	 : Lấy giá trị trung bình của điểm F1 trên toàn bộ các lớp. 
 
Kỹ thuật phân chia dữ liệu (Data Splitting) Để đảm bảo các kết quả đánh giá phản ánh chính xác khả năng tổng quát hóa (generalization) của hệ thống khi gặp dữ liệu thực tế, tập dữ liệu gốc được chia thành các phần chuyên biệt:  
●	Tập huấn luyện (Training set): Cung cấp dữ liệu để mô hình học tập và cập nhật các trọng số.  
●	Tập kiểm định (Validation set): Dùng để đo lường độc lập hiệu năng của mô hình ở mỗi vòng lặp (epoch), làm cơ sở cho việc lưu lại phiên bản tốt nhất và kích hoạt cơ chế dừng sớm (early stopping).  
●	Chia tập có phân tầng (Stratified split): Kỹ thuật này bắt buộc phải được áp dụng để đảm bảo tỷ lệ phân bố của 30 nhãn trong cả tập huấn luyện và kiểm định đều tương đồng với tỷ lệ gốc. Điều này mang ý nghĩa sống còn trong việc giữ cho dữ liệu không bị sai lệch cấu trúc khi giải quyết bài toán mất cân bằng đa lớp.  
   
2.8. Cơ chế hỗ trợ ra quyết định: ghi đè theo từ khóa và giải thích bằng LLM   
Bên cạnh kết quả dự đoán lõi từ mô hình PhoBERT, hệ thống áp dụng thêm ba cơ chế bổ trợ dựa trên quy tắc (rule-based) và mô hình ngôn ngữ lớn (LLM). Sự kết hợp này nhằm tối ưu hóa toàn diện ba yếu tố: độ chính xác, tốc độ phản hồi và tính hữu ích cho người dùng cuối.  
1.	Phát hiện tín hiệu cảnh báo bằng Biểu thức chính quy (Regex-based Signal Detection)  
●	Cơ chế hoạt động: Hệ thống định nghĩa sẵn một tập các mẫu (pattern) đặc trưng cho những hành vi lừa đảo phổ biến (ví dụ: yêu cầu mã OTP, số CVV, đường link đăng nhập lạ, cài đặt ứng dụng không rõ nguồn gốc, hoặc các từ ngữ tạo áp lực khẩn cấp như "xác minh tài khoản", "tài khoản bị khóa").  
●	Mục đích: Cơ chế này hoạt động hoàn toàn độc lập với mô hình AI và phục vụ hai vai trò chính:  
○ Đánh giá trực quan: Đối chiếu từng câu trong tin nhắn với các mẫu regex để gán mức độ (an toàn, đáng chú ý, nguy hiểm), giúp làm nổi bật (highlight) các nội dung đáng ngờ cho người dùng dễ nhận biết.  
○ Cảnh báo thời gian thực (Real-time): Tính toán điểm rủi ro tức thời dựa trên số lượng mẫu khớp được ngay trong lúc người dùng đang nhập liệu, trước cả khi gọi đến PhoBERT. Ưu điểm của cơ chế này là chi phí tính toán cực thấp, mang lại tốc độ phản hồi tức thì.  
2.	Ghi đè nhãn dựa trên từ khóa (Keyword-based Label Override)  
●	Cơ chế hoạt động: Mỗi loại hình lừa đảo trong hệ thống được gắn liền với một tập từ khóa đặc trưng (ví dụ: loại "lừa đảo đặt bàn" sẽ đi kèm các từ "đặt bàn", "nhà hàng", "giữ chỗ"). Khi PhoBERT dự đoán ra một nhãn lừa đảo nhưng nội dung tin nhắn lại không chứa từ khóa đặc trưng của nhãn đó, hệ thống sẽ tự động quét các nhãn có xác suất cao tiếp theo để tìm nhãn phù hợp hơn và tiến hành thay thế (ghi đè). Nếu vẫn không tìm thấy, kết quả sẽ chuyển thành "chưa chắc chắn" (uncertain).  
●	Mục đích: Đóng vai trò như một màng lọc hậu xử lý (post-processing). Bước này giúp khắc phục hiệu quả các sai số của AI trong những trường hợp nhầm lẫn giữa các loại hình lừa đảo có văn phong ngữ nghĩa gần giống nhau.  
3.	Sinh nội dung giải thích bằng LLM (LLM-based Explanation)  
●	Cơ chế hoạt động: Trong trường hợp hệ thống phát hiện tin nhắn lừa đảo hoặc rơi vào trạng thái "chưa chắc chắn", một luồng xử lý sẽ gọi đến mô hình ngôn ngữ lớn (Google Gemini) để tự động sinh ra một văn bản giải thích chi tiết, có cấu trúc rõ ràng bao gồm: loại hình chiêu thức, mô tả bản chất, các bước thực hiện của kẻ gian, dấu hiệu nhận biết (red flags), lời khuyên xử lý và hướng dẫn khắc phục nếu đã lỡ sập bẫy.  
●	Mục đích: Tận dụng điểm mạnh của cả hai loại mô hình. Mô hình PhoBERT chuyên biệt đảm nhiệm việc phân loại với tốc độ cao và chi phí thấp; trong khi LLM tổng quát bù đắp khả năng diễn giải ngôn ngữ phong phú, cung cấp thông tin cảnh báo dễ hiểu, có giá trị thực tiễn cao cho người dùng – điều mà một mô hình phân loại đơn thuần không thể làm được.  
Tổng quan luồng hoạt động tích hợp Nhìn chung, ba cơ chế trên được thiết kế để bổ trợ chéo cho nhau tại các thời điểm khác nhau trong vòng đời của một yêu cầu phân tích:  
●	(1) Phát hiện theo Regex: Hoạt động đầu tiên và liên tục, tốc độ cực cao, đóng vai trò cảnh báo sớm và hỗ trợ giao diện trực quan.  
●	(2) Ghi đè theo Keyword: Hoạt động ngay sau bước suy luận của PhoBERT, đóng vai trò kiểm tra chéo và tinh chỉnh độ chính xác.  
●	(3) Giải thích bằng LLM: Hoạt động ở bước cuối cùng, đóng vai trò "phiên dịch" kết quả kỹ thuật khô khan thành lời khuyên hữu ích cho người dùng.  
  
2.9. Các công cụ và công nghệ sử dụng  
Để xây dựng và triển khai hệ thống, đề tài sử dụng Python làm ngôn ngữ lập trình chủ đạo cho cả quá trình huấn luyện AI và phát triển backend, nhờ vào hệ sinh thái thư viện khổng lồ hỗ trợ đắc lực cho học sâu và xử lý ngôn ngữ tự nhiên. Cụ thể, các công nghệ được chia thành các nhóm sau:  
●	Framework học sâu và Quản lý mô hình:  
0	PyTorch: Được sử dụng làm framework học sâu nền tảng để xây dựng và huấn luyện mạng nơ-ron.  
○	Hugging Face Transformers: Đóng vai trò là thư viện giao tiếp chính với mô hình ngôn ngữ. Thư viện cung cấp các lớp AutoTokenizer và  
AutoModelForSequenceClassification, cho phép tải, tinh chỉnh (fine-tune) và chạy suy luận mô hình PhoBERT một cách thuận tiện thông qua một giao diện thống nhất.  
●	Xây dựng Backend và API:  
0	FastAPI: Framework web hiện đại được dùng để xây dựng các API phục vụ phân tích tin nhắn, quản lý người dùng và lịch sử. Ưu điểm nổi bật của FastAPI là kiến trúc xử lý bất đồng bộ (asynchronous), khả năng tự động sinh tài liệu API, và tích hợp sâu với thư viện Pydantic để kiểm tra tính hợp lệ của dữ liệu đầu vào.  
●	Lưu trữ dữ liệu:  
0	SQLite: Được chọn làm hệ quản trị cơ sở dữ liệu chính để lưu trữ thông tin tài khoản và lịch sử phân tích. Với đặc thù là cơ sở dữ liệu dạng tệp (file-based) không yêu cầu cài đặt máy chủ (server) riêng biệt, SQLite cực kỳ phù hợp và tối ưu cho các ứng dụng có quy mô vừa và nhỏ.  
●	Xác thực và Bảo mật:  
0	JSON Web Token (JWT): Thông qua thư viện python-jose, hệ thống cấp phát và xác thực token trong các phiên đăng nhập của người dùng.  
○	Bcrypt: Thư viện mã hóa được sử dụng để băm (hash) mật khẩu người dùng trước khi lưu vào cơ sở dữ liệu, đảm bảo nguyên tắc bảo mật là không bao giờ lưu trữ mật khẩu dưới dạng văn bản thuần (plaintext).  
●	Tích hợp Dịch vụ Trí tuệ nhân tạo bên ngoài:  
0	Google Gemini API: Thông qua thư viện google-generativeai, hệ thống tích hợp mô hình gemini-2.5-flash-lite nhằm thực hiện hai chức năng nâng cao:  
1.	Trích xuất văn bản tự động từ ảnh chụp màn hình tin nhắn (OCR).  
2.	Sinh nội dung giải thích chi tiết và đưa ra lời khuyên xử lý cho các kết quả phân loại  
  
  
 
 
 
 
CHƯƠNG 3: PHÂN TÍCH VÀ THIẾT KẾ HỆ THỐNG  
  
3.1. Quy trình tổng quan của hệ thống  
Hệ thống ScamShield được xây dựng theo kiến trúc client-server, trong đó phần backend (FastAPI) đóng vai trò xử lý toàn bộ logic phân tích, còn phần frontend chịu trách nhiệm tiếp nhận đầu vào và hiển thị kết quả.  
   
Hình 5 : Giao diện của hệ thống  
Quy trình xử lý một yêu cầu phân tích đầy đủ (qua endpoint /analyze hoặc /analyze/image) trải qua 6 bước chính như sau:  
3.1.1 Tiếp nhận và chuẩn hóa đầu vào Hệ thống linh hoạt hỗ trợ ba định dạng dữ liệu đầu vào:  
●	Văn bản đơn: Đoạn tin nhắn liên tục được chuẩn hóa Unicode và loại bỏ khoảng trắng dư thừa.  
●	Hội thoại nhiều lượt: Hệ thống trích xuất 8 lượt trao đổi gần nhất, sau đó ghép nối thành một đoạn văn bản duy nhất, phân tách nhau bằng thẻ [SEP].  
●	Hình ảnh (Ảnh chụp màn hình): Hệ thống gọi API Gemini để thực hiện nhận dạng ký tự quang học (OCR). Nội dung văn bản được trích xuất, sắp xếp lại theo thứ tự hội thoại (phân biệt người gửi/nhận) và đưa vào xử lý như văn bản thông thường.  
3.1.2 Phân loại bằng mô hình PhoBERT  
●	Văn bản sau chuẩn hóa được đưa qua Tokenizer để chuyển thành chuỗi token với độ dài cố định (max_length = 256).  
●	Chuỗi token được đưa vào mô hình PhoBERT đã tinh chỉnh để tính toán phân bố xác suất trên 30 nhãn thông qua hàm Softmax.  
●	Nhãn có xác suất cao nhất được chọn làm kết quả dự đoán ban đầu. Đồng thời, hệ thống tính toán điểm rủi ro (risk score) dựa trên tổng xác suất của các nhãn thuộc nhóm lừa đảo.  
3.1.3 Ghi đè nhãn dựa trên từ khóa (Keyword Override)  
●	Nếu nhãn dự đoán ban đầu là lừa đảo nhưng văn bản không chứa từ khóa đặc trưng của loại hình đó, hệ thống sẽ duyệt qua các nhãn có xác suất cao tiếp theo để tìm nhãn phù hợp hơn và tiến hành ghi đè.  
●	Nếu không có nhãn nào khớp từ khóa, kết quả được đưa về trạng thái "chưa chắc chắn" (uncertain).  
●	Đầu ra của bước này cung cấp: nhãn cuối cùng, tên loại hình, và danh sách top 3 nhãn có xác suất cao nhất.  
3.1.4  Phát hiện tín hiệu cảnh báo theo mẫu (Regex Highlighting)  
●	Xử lý song song với các bước trên, văn bản được tách thành từng câu.  
●	Mỗi câu được đối chiếu với tập biểu thức chính quy (Regex) đặc trưng cho các hành vi lừa đảo để gán mức độ: an toàn, đáng chú ý, hoặc nguy hiểm.  
●	Dữ liệu này giúp giao diện frontend tô màu (highlight) các câu đáng ngờ để người dùng dễ nhận biết.  
3.1.5 Sinh giải thích chi tiết bằng LLM  
●	Kích hoạt khi kết quả ở Bước 3 là lừa đảo  
●	Hệ thống gửi yêu cầu đến Gemini để sinh văn bản giải thích có cấu trúc gồm: tên loại hình, mô tả ngắn, các bước điển hình, dấu hiệu nhận biết, và lời khuyên xử lý.  
3.1.6 Trả kết quả và lưu trữ  
●	Toàn bộ dữ liệu tổng hợp (trạng thái, điểm rủi ro, tên loại hình, độ tin cậy, top nhãn liên quan, câu highlight và nội dung giải thích) được đóng gói dưới định dạng JSON và trả về cho frontend.  
●	Nếu người dùng đã đăng nhập, frontend sẽ gọi một endpoint riêng để lưu lại lịch sử phân tích vào cơ sở dữ liệu SQLite.  
Hình 6: Sơ đồ tổng quan của hệ thống 
3.2. Phân tích và chuẩn bị dữ liệu   
3.2.1. Nguồn dữ liệu và Quy mô tổng thể Dữ liệu huấn luyện của hệ thống được thu thập và tổ chức thành hai tệp JSON riêng biệt:  
●	Tập dữ liệu lừa đảo (scam_with_metadata_fixed.json): Chứa 2000 mẫu tin nhắn có dấu hiệu lừa đảo.  
●	Tập dữ liệu an toàn (tong_hop_dataset_antoan_.json): Chứa 2000 mẫu tin nhắn giao tiếp thông thường, không chứa yếu tố lừa đảo. Dataset gốc có thể có nhiều mẫu an 
toàn hơn, nhưng hệ thống chủ động cap (giới hạn) xuống 1000 bằng 
HARMLESS_CAP để mẫu an toàn không áp đảo, đảm bảo WeightedRandomSampler hoạt động hiệu quả hơn trên các nhãn lừa đảo thiểu số 
●	Đánh giá chung: Tổng số lượng của toàn bộ tập dữ liệu là 3000 mẫu. Với data đa dạng và không trùng nhau về mặt ngữ nghĩa đủ phục vụ tối cho hệ thống có kết quả tốt   
3.2.2. Cấu trúc dữ liệu và Siêu dữ liệu (Metadata) Mỗi mẫu dữ liệu lừa đảo được lưu trữ dưới dạng một đối tượng JSON với cấu trúc chi tiết như sau:  
●	Thông tin định danh: label (mã số) và label_name (tên gọi) xác định chính xác loại hình lừa đảo.  
●	Nội dung chính (dialogue): Chứa nội dung văn bản dưới dạng một danh sách các lượt trao đổi. Mỗi lượt bao gồm role (vai trò người gửi, ví dụ: "người gọi", "người nghe") và content (nội dung lời nói/tin nhắn).  
●	Siêu dữ liệu (Metadata): Bao gồm các trường mô tả ngữ cảnh như channel (Zalo, SMS, gọi điện), hour_sent, url_list, phone_list, email_list, is_first_contact (lần liên hệ đầu tiên) và risk_score (điểm rủi ro tham khảo).  
0	Vai trò của Metadata: Mặc dù không phải là đầu vào trực tiếp cho mô hình PhoBERT, các siêu dữ liệu này có giá trị tham khảo cốt lõi trong việc xây dựng và kiểm chứng các quy tắc phát hiện tín hiệu cảnh báo (đã trình bày ở phần 2.8).  
3.2.3. Phân bố nhãn và Bài toán mất cân bằng dữ liệu Dù cân bằng ở cấp độ tổng thể, dữ liệu lại đối mặt với bài toán mất cân bằng (class imbalance) trầm trọng khi xét trên cấu trúc phân loại 30 lớp:  
●	Nhóm an toàn (Nhãn 0): Chiếm tới 1000 mẫu.  
●	Nhóm lừa đảo (Nhãn 1 đến 29): 2000 mẫu được chia cho 29 loại hình khác nhau. Số lượng dao động từ 32 đến 106 mẫu/loại (trung bình khoảng 68 mẫu).  
0	Nhiều nhất: "Lừa đảo vay vốn" (106 mẫu).  
○ Ít nhất: "Lừa đảo giả danh cơ quan thuế" (42 mẫu).  
●	Giải pháp: Sự chênh lệch khổng lồ giữa lớp đa số (an toàn) và từng lớp thiểu số (lừa đảo) chính là cơ sở thực tiễn bắt buộc hệ thống phải áp dụng kỹ thuật lấy mẫu có trọng số (Weighted Random Sampling) trong quá trình huấn luyện (như đã phân tích ở phần 2.6), giúp mô hình học đều các đặc trưng của mọi loại hình lừa đảo mà không bị lớp an toàn chi phối.  
3.2.4. Tiền xử lý và Chuẩn hóa dữ liệu Trước khi đưa vào huấn luyện, hai tệp JSON trải qua giai đoạn tiền xử lý nghiêm ngặt:  
●	Gộp tập dữ liệu: Đọc và đồng nhất hai tệp dữ liệu, trong đó toàn bộ 1000 mẫu thuộc tệp an toàn được gán tự động thành nhãn 0.  
●	Làm sạch lỗi thủ công: Phát hiện và xử lý các lỗi dữ liệu sinh ra trong quá trình thu thập và gán nhãn bằng tay (ví dụ: trường hợp label_name bị viết sai chính tả hoặc thiếu dấu câu). Việc này đảm bảo tính nhất quán tuyệt đối của tập nhãn trước khi đưa vào mạng nơ-ron.  
3.3. Tiền xử lý dữ liệu văn bản  
Trước khi đưa vào mô hình PhoBERT, dữ liệu văn bản thô cần trải qua một số bước tiền xử lý nhằm đưa về dạng chuẩn, phù hợp với định dạng đầu vào mà mô hình yêu cầu. Các bước này được thực hiện theo thứ tự sau:  
●	Chuẩn hóa văn bản (Text Normalization):  
0	Mục đích: Đảm bảo văn bản có định dạng nhất quán trước khi xử lý tiếp.  ○ Cách thực hiện: Văn bản được chuẩn hóa theo dạng Unicode NFC (chuẩn hóa cách biểu diễn dấu tiếng Việt), đồng thời loại bỏ các khoảng trắng, ký tự xuống dòng dư thừa. Bước này giúp tránh trường hợp cùng một ký tự tiếng Việt nhưng được biểu diễn dưới nhiều dạng mã Unicode khác nhau, có thể gây ảnh hưởng đến quá trình tách từ của tokenizer.  
●	Xử lý dữ liệu dạng hội thoại nhiều lượt (Dialogue Processing):  
0	Vấn đề: Nhiều mẫu dữ liệu được lưu dưới dạng một danh sách các lượt trao đổi (dialogue) giữa hai phía, trong khi mô hình PhoBERT chỉ nhận đầu vào là một chuỗi văn bản duy nhất.  
○	Cách thực hiện: Nếu một mẫu có nhiều hơn 8 lượt trao đổi, hệ thống chỉ giữ lại 8 lượt cuối cùng - đây là phần thường chứa các nội dung quyết định như yêu cầu chuyển khoản, cung cấp mã OTP. Các lượt được giữ lại sau đó được ghép thành một chuỗi văn bản duy nhất, với mỗi lượt được phân tách bằng token đặc biệt [SEP], giúp mô hình nhận biết được ranh giới giữa các lượt trao đổi khi học biểu diễn.  
●	Tách từ và mã hóa (Tokenization):  
0	Mục đích: Chuyển văn bản (dạng chuỗi ký tự) thành dạng số mà mô hình có thể xử lý được.  
○	Cách thực hiện: Văn bản sau khi chuẩn hóa và ghép lượt được đưa qua tokenizer riêng của PhoBERT (đi kèm với mô hình vinai/phobert-base-v2), vốn được xây dựng chuyên biệt để xử lý tốt đặc điểm từ ghép trong tiếng Việt. Tokenizer này chuyển văn bản thành một chuỗi các token (đơn vị từ/âm tiết) tương ứng với các chỉ số trong từ điển của mô hình.  
●	Chuẩn hóa độ dài đầu vào (Padding & Truncation):  
0	Vấn đề: Các mẫu văn bản có độ dài khác nhau, trong khi mô hình yêu cầu đầu vào có kích thước cố định trong mỗi batch huấn luyện.  
○	Cách thực hiện: Độ dài chuỗi token được giới hạn ở mức max_length = 
256. Nếu chuỗi token ngắn hơn 256, các vị trí còn thiếu sẽ được điền 
(padding) bằng token đặc biệt; nếu dài hơn 256, phần vượt quá sẽ bị cắt bỏ (truncation). Kết quả đầu ra của bước này là hai ma trận số: input_ids (chỉ số token) và attention_mask (đánh dấu vị trí nào là dữ liệu thật, vị trí nào là padding), đây chính là định dạng đầu vào cuối cùng được đưa vào mô hình PhoBERT.  
3.4. Tăng cường dữ liệu (Data Augmentation)  
Như đã phân tích ở phần 3.2, mỗi loại hình lừa đảo trong số 29 nhóm chỉ có trung bình khoảng 68 mẫu dữ liệu (dao động từ 32 đến 106 mẫu), một số lượng còn khá hạn chế để mô hình học được đầy đủ các cách diễn đạt khác nhau của từng chiêu thức. Do đó, quá trình tăng cường dữ liệu được thực hiện theo hai phương pháp kết hợp như sau:  
●	Sinh dữ liệu bằng AI (AI-generated Dialogue):  
0	Mục đích: Tạo ra số lượng lớn các đoạn hội thoại mới với nội dung và cách diễn đạt đa dạng, mô phỏng các tình huống lừa đảo khác nhau trong cùng một loại hình.  
○	Cách thực hiện: Sử dụng mô hình ngôn ngữ lớn để sinh hội thoại, dựa trên việc cung cấp thông tin định hướng cho từng loại hình lừa đảo như: bối cảnh tình huống, vai trò của các bên tham gia hội thoại, mục tiêu mà đối tượng lừa đảo muốn đạt được, và các yếu tố đặc trưng cần xuất hiện (ví dụ yêu cầu chuyển khoản, mã OTP, đường link...). Từ đó, mô hình tạo ra các đoạn hội thoại mới có nội dung khác biệt nhưng vẫn giữ đúng bản chất và nhãn của loại hình lừa đảo tương ứng.  
○ Ưu điểm: Tạo ra số lượng mẫu lớn trong thời gian ngắn, với sự đa dạng cao về ngữ cảnh, cách xưng hô và tình huống - giúp mô hình tránh học theo các khuôn mẫu câu chữ cố định.  
●	Viết tay theo mẫu (Template-based Augmentation):  
0	Mục đích: Đảm bảo các mẫu dữ liệu mới vẫn sát với thực tế và giữ đúng các đặc trưng quan trọng của từng loại hình lừa đảo.  
○	Cách thực hiện: Dựa trên các mẫu hội thoại lừa đảo thực tế đã thu thập được, xây dựng các khung mẫu (template) chung cho từng loại hình, trong đó các chi tiết có thể thay đổi - như tên tổ chức/cá nhân giả mạo, số tiền, số điện thoại, đường dẫn, thời gian, kênh liên lạc - được hoán đổi để tạo ra nhiều biến thể khác nhau từ cùng một kịch bản gốc.  
○ Ưu điểm: Đảm bảo độ chính xác và tính đặc trưng cao, do được xây dựng trực tiếp từ các kịch bản lừa đảo đã được kiểm chứng trong thực tế.  
●	Kết hợp hai phương pháp:  
0	Hai phương pháp trên được sử dụng bổ trợ cho nhau: dữ liệu sinh bằng AI mang lại sự đa dạng và số lượng, còn dữ liệu viết tay theo mẫu đảm bảo độ chính xác và tính sát thực tế. Nhờ kết hợp cả hai, tập dữ liệu cho mỗi loại hình lừa đảo được mở rộng với cả số lượng và độ đa dạng cần thiết, giúp mô hình PhoBERT học được các đặc trưng ngôn ngữ chung của từng chiêu thức, đồng thời hạn chế hiện tượng quá khớp (overfitting) vào một số cách diễn đạt cố định.  
●	Định hướng mở rộng tiếp theo:  
0	Đối với các loại hình lừa đảo còn ít mẫu nhất (ví dụ "Lừa đảo giả danh cơ quan thuế" với 32 mẫu, "Lừa đảo máy lọc nước" với 35 mẫu), việc tiếp tục sinh thêm dữ liệu theo hai phương pháp trên là hướng cải thiện được đề xuất, nhằm thu hẹp khoảng cách số lượng mẫu giữa các nhãn và nâng cao hơn nữa độ chính xác phân loại cho các nhóm này.  
3.5. Thiết kế kiến trúc mô hình PhoBERT  
Kiến trúc mô hình được sử dụng trong đề tài dựa trên nguyên lý "mô hình nền + lớp phân loại" (backbone + classification head), tận dụng khả năng biểu diễn ngôn ngữ đã học được từ PhoBERT và bổ sung một lớp đầu ra phù hợp với bài toán 30 nhãn. Kiến trúc cụ thể bao gồm các thành phần sau:  
●	Mô hình nền - PhoBERT backbone:  
0	Thành phần: Sử dụng phiên bản vinai/phobert-base-v2, được tải thông qua lớp AutoModelForSequenceClassification của thư viện Hugging Face Transformers.  
○	Vai trò: Đóng vai trò là bộ trích xuất đặc trưng (feature extractor), nhận đầu vào là chuỗi token đã được tiền xử lý (input_ids, attention_mask) và trả về các vector biểu diễn ngữ nghĩa của văn bản, được học thông qua nhiều lớp encoder Transformer xếp chồng, mỗi lớp gồm cơ chế tự chú ý đa đầu (multihead selfattention) và mạng truyền thẳng (feed-forward network).  
●	Lớp phân loại (Classification Head):  
0	Thành phần: Một lớp tuyến tính (linear layer) được gắn thêm vào sau backbone, với số đầu ra bằng đúng số lượng nhãn của bài toán (num_labels = 30).  
○	Vai trò: Nhận biểu diễn tổng hợp của toàn bộ văn bản từ backbone và chuyển đổi thành 30 giá trị (logits), mỗi giá trị tương ứng với một nhãn trong tập 30 nhãn (1 nhãn "không phải lừa đảo" và 29 nhãn loại hình lừa đảo cụ thể).  
●	Hàm kích hoạt đầu ra - Softmax:  
0	Vai trò: Áp dụng lên 30 giá trị logits để chuyển đổi thành một phân bố xác suất, trong đó tổng xác suất của tất cả các nhãn bằng 1. Nhãn có xác suất cao nhất được chọn làm kết quả dự đoán, đồng thời toàn bộ phân bố xác suất này được sử dụng cho các bước xử lý phía sau như tính điểm rủi ro và xác định độ tin cậy .  
●	Kỹ thuật đóng băng tham số (Layer Freezing):  
0	Vấn đề: Nếu huấn luyện (cập nhật trọng số) toàn bộ mô hình PhoBERT - bao gồm cả các lớp embedding và encoder ở tầng thấp, vốn đã học được các đặc trưng ngôn ngữ tiếng Việt tổng quát từ giai đoạn tiền huấn luyện - có thể làm mô hình "quên" đi các tri thức ngôn ngữ tổng quát này (hiện tượng catastrophic forgetting), đồng thời làm tăng đáng kể thời gian huấn luyện và yêu cầu phần cứng.  
○	Cách thực hiện: Đóng băng (freeze) lớp embedding và 6 lớp encoder đầu tiên của PhoBERT, tức là không cập nhật trọng số của các thành phần này trong quá trình huấn luyện (requires_grad = False). Chỉ các lớp encoder còn lại (các lớp ở tầng cao hơn) và lớp phân loại mới được cập nhật trọng số.  ○ Lợi ích: Giữ lại được các đặc trưng ngôn ngữ tổng quát (từ vựng, ngữ pháp tiếng Việt) đã học từ giai đoạn tiền huấn luyện ở các lớp dưới, đồng thời cho phép các lớp trên và lớp phân loại học chuyên biệt cho bài toán phân loại tin nhắn lừa đảo. Cách làm này còn giúp giảm số lượng tham số cần cập nhật, từ đó giảm thời gian huấn luyện và nguy cơ overfitting khi huấn luyện trên tập dữ liệu có quy mô vừa và nhỏ  
●	Luồng dữ liệu qua mô hình (Data Flow):  
0	Văn bản đầu vào (đã tokenize) → đi qua lớp embedding (đã đóng băng) → qua các lớp encoder Transformer (6 lớp đầu đóng băng, các lớp còn lại được tinh chỉnh) → vector biểu diễn của văn bản → lớp phân loại (classification head) → 30 giá trị logits → hàm Softmax → phân bố xác suất trên 30 nhãn.  
  
3.6. Cấu hình và huấn luyện mô hình  
Quá trình huấn luyện mô hình được thực hiện theo một quy trình có cấu hình rõ ràng và cơ chế kiểm soát chặt chẽ nhằm đảm bảo mô hình đạt hiệu quả tốt nhất trên tập dữ liệu hiện có. Các thành phần chính của quá trình này như sau:  
●	Cấu hình huấn luyện (Training Configuration):  
	0 	Mô hình nền: vinai/phobert-base-v2.  
○	Độ dài chuỗi token tối đa (MAX_LEN): 256.  
○ Kích thước batch (BATCH_SIZE): 16 mẫu mỗi lượt cập nhật trọng số.  ○ Số epoch tối đa (EPOCHS): 15, kết hợp với cơ chế dừng sớm để không nhất thiết phải chạy hết số epoch này.  
○ Tốc độ học (LEARNING_RATE): 2e-5 - một giá trị nhỏ, phù hợp với giai đoạn tinh chỉnh (fine-tuning) các mô hình ngôn ngữ tiền huấn luyện, giúp tránh làm thay đổi quá lớn các trọng số đã học.  
○ Thiết bị tính toán (DEVICE): tự động lựa chọn GPU (CUDA) nếu khả dụng, ngược lại sử dụng CPU.  
●	Chia tập dữ liệu (Train/Validation Split):  
0 	Tập dữ liệu sau khi gộp và chuẩn hóa được chia thành tập huấn luyện và tập kiểm định theo tỷ lệ 85/15, sử dụng kỹ thuật chia có phân tầng (stratify) để đảm bảo tỷ lệ các nhãn trong hai tập tương đồng với tỷ lệ trong toàn bộ dữ liệu  ● Cơ chế lấy mẫu cân bằng (Weighted Sampling cho tập huấn luyện):  
○	Riêng tập huấn luyện được nạp dữ liệu thông qua  
WeightedRandomSampler, trong đó mỗi mẫu được gán trọng số lấy mẫu 
bằng 1 chia cho số lượng mẫu của nhãn tương ứng. Nhờ đó, trong mỗi epoch, các mẫu thuộc các nhãn lừa đảo ít dữ liệu được lấy ra (oversample) với tần suất cao hơn, giúp mô hình tiếp xúc cân bằng hơn với cả 30 nhãn  
●	Hàm mất mát và bộ tối ưu (Loss & Optimizer):  
○ Hàm mất mát: CrossEntropyLoss - hàm mất mát tiêu chuẩn cho bài toán phân loại đa lớp. Do việc mất cân bằng dữ liệu đã được xử lý ở bước lấy mẫu, hàm mất mát không cần áp dụng thêm trọng số theo lớp.   
𝑁
	𝐿  	𝑙 𝑙𝑜𝑔 𝑃   
𝑖 
Trong đó:  
•	𝓛: Giá trị hàm mất mát (loss) trung bình trên toàn bộ batch. 
•	N: Tổng số mẫu trong một batch huấn luyện (trong đề tài: N = 16 do BATCH_SIZE = 16). 
•	x_i: Văn bản đầu vào của mẫu thứ i sau khi đã tokenize. 
•	y_i: Nhãn thật (ground truth) của mẫu thứ i, với y_i ∈ {0, 1, ..., 29}. 
•	P(y = y_i | x_i): Xác suất mô hình dự đoán đúng nhãn thật y_i cho mẫu x_i, được tính từ đầu ra Softmax. 
•	log: Logarithm tự nhiên — phạt nặng khi xác suất dự đoán đúng gần bằng 0, phạt nhẹ khi gần bằng 1. 
•	Dấu "−": Đảm bảo giá trị loss luôn dương, vì log(P) ≤ 0 khi P ∈ (0, 1]. 
Ý nghĩa thực tiễn: 
Mô hình được tối ưu bằng cách tối thiểu hóa 𝓛, tức là buộc xác suất dự đoán đúng nhãn thật càng cao càng tốt. Khi mô hình dự đoán chắc chắn và đúng (P → 1), loss tiến về 0. Khi dự đoán sai hoặc không chắc (P → 0), loss tăng mạnh.  
○ Bộ tối ưu: AdamW, chỉ áp dụng cập nhật cho các tham số chưa bị đóng băng  , Weight decay được áp dụng trực tiếp lên tham số thông qua số hạng 𝜆𝜃𝑡(decoupled weight decay). 
So sánh AdamW và Adam tiêu chuẩn: Sự khác biệt cốt lõi giữa hai bộ tối ưu này nằm ở cách xử lý weight decay (suy giảm trọng số) — kỹ thuật regularization nhằm hạn chế overfitting bằng cách kéo các trọng số về gần 0. 
Trong Adam tiêu chuẩn, weight decay được cộng trực tiếp vào gradient trước khi tính các moment bậc một và bậc hai: 
𝑔𝑡 = 𝛻ℒ(𝜃𝑡) + 𝜆𝜃𝑡 
> Hệ quả là weight decay bị "trộn lẫn" vào quá trình tính trung bình động của Adam, làm cho hiệu quả thực tế của weight decay phụ thuộc vào tốc độ học và các tham số 𝛽1, 𝛽2— gây khó kiểm soát. 
AdamW (Loshchilov & Hutter, 2019) tách hoàn toàn weight decay ra khỏi bước tính gradient, cộng trực tiếp vào bước cập nhật tham số cuối cùng (decoupled weight decay), thể hiện qua số hạng 𝜆𝜃𝑡độc lập trong công thức cập nhật ở phần trên. Nhờ tách biệt này, weight decay hoạt động đúng với ý nghĩa ban đầu , co trọng số về 0 với cường độ cố định không bị ảnh hưởng bởi quy mô gradient. 
Đối với bài toán fine-tune PhoBERT trên tập dữ liệu vừa và nhỏ (~3000 mẫu), AdamW giúp kiểm soát overfitting hiệu quả hơn Adam tiêu chuẩn, đây là lý do AdamW được sử dụng rộng rãi khi fine-tune các mô hình BERT/RoBERTa trong thực tế. 
 
𝑚ˆ𝑡
𝜃𝑡+1 = 𝜃𝑡 − 𝛼 (  + 𝜆𝜃𝑡) 
√𝑣ˆ𝑡 + 𝜖 Trong đó: 
●	𝜃𝑡: Giá trị tham số của mô hình tại bước cập nhật thứ 𝑡.  
●	𝜃𝑡+1: Giá trị tham số sau khi được cập nhật.  
●	𝛼: Learning rate (tốc độ học), quyết định kích thước bước cập nhật tham số.  
●	𝜆: Hệ số Weight Decay (L2 Regularization), dùng để giảm độ lớn của trọng số nhằm hạn chế hiện tượng overfitting.  
●	𝑚̂𝑡: Moment bậc một đã hiệu chỉnh bias (bias-corrected first moment estimate), tương ứng với trung bình động của gradient.  
●	𝑣̂𝑡: Moment bậc hai đã hiệu chỉnh bias (bias-corrected second moment estimate), tương ứng với trung bình động của bình phương gradient.  
●	𝜖: Một hằng số rất nhỏ (thường là 10−8) để tránh chia cho 0.  
●	𝑡: Chỉ số bước lặp trong quá trình tối ưu. 
⇨ Nhờ đó, AdamW thường cho hiệu quả tổng quát hóa tốt hơn và hiện được sử dụng rộng rãi trong các mô hình học sâu hiện đại như BERT 
●	Vòng lặp huấn luyện (Training Loop):  
0	Trong mỗi epoch, mô hình được đưa vào chế độ huấn luyện (train mode), lặp qua từng batch dữ liệu từ tập huấn luyện: tính toán đầu ra (logits), tính giá trị hàm mất mát so với nhãn thật, lan truyền ngược (backpropagation) và cập nhật trọng số thông qua bộ tối ưu.  
○	Sau khi hoàn tất một epoch, mô hình được chuyển sang chế độ đánh giá (eval mode) và chạy dự đoán trên toàn bộ tập kiểm định, không cập nhật trọng số.  
●	Đánh giá và lưu mô hình tốt nhất:  
0	Sau mỗi epoch, chỉ số macro-F1 trên tập kiểm định được tính toán dựa trên kết quả dự đoán và nhãn thật. Nếu chỉ số này cao hơn giá trị tốt nhất đã ghi nhận trước đó, mô hình (cùng tokenizer) sẽ được lưu lại, đồng thời ghi đè giá trị macro-F1 tốt nhất.  
○	Cùng với việc lưu mô hình, một tệp meta.json cũng được tạo/cập nhật, chứa thông tin ánh xạ nhãn (id2label) và ngưỡng tin cậy (conf_threshold), phục vụ cho việc nạp lại mô hình ở phía backend.  
●	Cơ chế dừng sớm (Early Stopping):  
0	Hệ thống theo dõi số epoch liên tiếp mà macro-F1 trên tập kiểm định không cải thiện (patience_counter). Nếu số epoch không cải thiện đạt đến ngưỡng patience = 4, quá trình huấn luyện sẽ dừng lại trước khi đạt đến EPOCHS = 15, nhằm tránh huấn luyện thêm không cần thiết và giảm nguy cơ overfitting.  
●	Báo cáo kết quả huấn luyện:  
0	Sau khi quá trình huấn luyện kết thúc (do hết epoch hoặc do early stopping), hệ thống in ra báo cáo phân loại chi tiết (classification_report) trên tập kiểm định tại thời điểm mô hình tốt nhất, bao gồm precision, recall và F1-score cho từng nhãn trong số 30 nhãn - cung cấp cơ sở để đánh giá hiệu quả mô hình trên từng loại hình lừa đảo cụ thể.  
3.7. Lưu trữ và tải mô hình  
Sau khi hoàn tất quá trình huấn luyện, mô hình cần được lưu lại dưới một định dạng có thể nạp lại dễ dàng ở phía backend để phục vụ suy luận. Quy trình lưu trữ và tải mô hình được thực hiện như sau:  
●	Lưu mô hình sau huấn luyện:  
-Thành phần được lưu: Trọng số của mô hình PhoBERT đã tinh chỉnh và tokenizer tương ứng, được lưu thông qua các hàm save_pretrained() của thư viện Hugging Face Transformers vào một thư mục cố định (SAVE_DIR).  -Thời điểm lưu: Mỗi khi mô hình đạt được chỉ số macro-F1 tốt hơn giá trị tốt nhất đã ghi nhận trước đó (như đã trình bày ở phần 3.6), toàn bộ mô hình và tokenizer tại thời điểm đó sẽ được lưu lại, đảm bảo phiên bản cuối cùng được lưu luôn là phiên bản có hiệu quả cao nhất trên tập kiểm định.  
●	Tệp metadata (meta.json):  
-Nội dung: Bao gồm bảng ánh xạ từ chỉ số nhãn sang tên loại hình lừa đảo (id2label), và ngưỡng tin cậy (conf_threshold = 0.50) dùng để xác định khi nào kết quả dự đoán được coi là "chưa chắc chắn". Cụ thể, nếu xác suất Softmax của nhãn có điểm cao nhất nhỏ hơn 0.50, hệ thống coi đây là một dự đoán không đủ tin cậy và kích hoạt cơ chế ghi đè theo từ khóa (Keyword Override, đã trình bày ở mục 2.8 và 3.1.3) trước khi đưa ra kết quả cuối cùng cho người dùng. Việc chọn ngưỡng 0.50 — tức điểm giữa của khoảng xác suất [0,1] — phản ánh nguyên tắc "nghiêng về an toàn" (safety-first): bất kỳ dự đoán nào có độ tin cậy dưới mức trung bình đều cần được xác minh thêm trước khi kết luận. 
-Vai trò: Tách riêng các thông tin cấu hình liên quan đến nhãn và ngưỡng ra khỏi mã nguồn, giúp backend có thể đọc và áp dụng các thông tin này một  
cách linh hoạt mà không cần sửa code khi cần thay đổi (ví dụ điều chỉnh ngưỡng tin cậy).  
●	Tải mô hình khi khởi động backend:  
-Cơ chế: Khi ứng dụng FastAPI khởi động (sự kiện startup), hàm load_models() được gọi để thực hiện việc nạp mô hình.  
-Quy trình tải: Đầu tiên, hệ thống đọc tệp meta.json (nếu tồn tại) để cập nhật bảng ánh xạ nhãn và ngưỡng tin cậy. Tiếp theo, tokenizer và mô hình  PhoBERT đã huấn luyện được tải từ thư mục lưu trữ thông qua  
AutoTokenizer.from_pretrained() và  
AutoModelForSequenceClassification.from_pretrained(), sau đó mô hình được chuyển sang chế độ đánh giá (eval mode) và đưa lên thiết bị tính toán phù hợp (GPU/CPU).  
-Cơ chế dự phòng: Nếu không tìm thấy thư mục mô hình hoặc quá trình tải gặp lỗi, hệ thống vẫn khởi động bình thường nhưng hàm predict() sẽ chuyển sang chế độ dự phòng dựa trên việc đối chiếu từ khóa đơn giản  (SCAM_SIGNALS), đảm bảo các endpoint vẫn hoạt động được ở mức tối thiểu trong khi chờ mô hình được cung cấp.  
● Tải mô hình hỗ trợ giải thích (Gemini):  
-Cùng trong hàm load_models(), mô hình Gemini (gemini-2.5-flash-lite) được khởi tạo thông qua API key, phục vụ cho các chức năng OCR ảnh và sinh giải thích đã trình bày ở phần 2.8.  
3.8. Thiết kế hệ thống xử lý (API Backend)  
Phần backend được xây dựng bằng FastAPI, cung cấp các API phục vụ việc phân tích tin nhắn, xác thực người dùng và quản lý lịch sử phân tích. Các API được tổ chức thành ba nhóm chính như sau:  
●	Nhóm API phân tích (Analyze):  
0	POST /analyze - nhận đầu vào là văn bản hoặc đoạn hội thoại, thực hiện toàn bộ pipeline đã trình bày ở phần 3.1 (tiền xử lý → PhoBERT → ghi đè từ khóa → phát hiện tín hiệu → giải thích bằng LLM nếu cần), trả về kết quả phân loại, điểm rủi ro, các câu được đánh dấu nguy hiểm và nội dung giải thích.  ○ POST /analyze/realtime - phiên bản nhẹ, chỉ áp dụng phát hiện tín hiệu theo mẫu (regex), dùng để cảnh báo nhanh trong lúc người dùng đang nhập tin nhắn.  
○	POST /analyze/image - nhận một tệp ảnh, thực hiện OCR bằng Gemini để trích xuất nội dung văn bản, sau đó áp dụng pipeline phân tích tương tự /analyze.  
○ POST /chat - cung cấp một chatbot hỏi đáp về phòng chống lừa đảo, sử dụng Gemini để trả lời dựa trên nội dung câu hỏi và lịch sử trò chuyện.  ○ GET /scam-types và GET /health - cung cấp danh sách các loại hình lừa đảo mà hệ thống có thể nhận diện, và thông tin trạng thái hoạt động của các thành phần (mô hình PhoBERT, Gemini, thiết bị tính toán).  
●	Nhóm API xác thực người dùng (Auth):  
0	POST /auth/register - tạo tài khoản mới, kiểm tra ràng buộc đầu vào (độ dài tên người dùng, mật khẩu, định dạng email), mật khẩu được băm bằng bcrypt trước khi lưu vào cơ sở dữ liệu.  
○	POST /auth/login - xác thực thông tin đăng nhập, trả về token truy cập (JWT) nếu hợp lệ.  
○ GET /auth/me - trả về thông tin tài khoản hiện tại dựa trên token, dùng để xác minh trạng thái đăng nhập ở phía frontend.  
○ Cơ chế xác thực: Các endpoint yêu cầu đăng nhập sử dụng cơ chế OAuth2 Bearer Token kết hợp JWT; token được mã hóa với thời hạn 7 ngày, và được kiểm tra thông qua một dependency chung (get_current_user) áp dụng cho mọi endpoint cần xác thực.  
●	Nhóm API quản lý lịch sử phân tích (Reports):  
0	POST /save-report - lưu kết quả của một lần phân tích (trạng thái lừa đảo, điểm rủi ro, độ tin cậy, nhãn, nội dung tin nhắn rút gọn, giải thích) vào bảng reports, gắn với người dùng đang đăng nhập.  
○	GET /my-reports - lấy danh sách lịch sử phân tích của người dùng hiện tại, hỗ trợ phân trang (limit, offset), sắp xếp theo thời gian gần nhất.  
○ DELETE /my-reports/{id} - xóa một bản ghi lịch sử, có kiểm tra quyền sở hữu để đảm bảo người dùng chỉ có thể xóa bản ghi của chính mình.  
●	Các thành phần hỗ trợ chung:  
0	Cơ sở dữ liệu: SQLite, gồm hai bảng users (thông tin tài khoản) và reports (lịch sử phân tích), được khởi tạo tự động khi backend khởi động lần đầu (init_db()).  
○	CORS Middleware: Cho phép frontend (chạy trên domain/port khác) có thể gọi đến các API của backend trong quá trình phát triển và triển khai.  
  
  
  
  
  
  
  
  
  
 
 
 
 
CHƯƠNG 4. KẾT QUẢ THỰC NGHIỆM VÀ ĐÁNH GIÁ  
Chương này trình bày chi tiết các kết quả thu được từ quá trình huấn luyện mô hình ngôn ngữ 
PhoBERT, đánh giá hiệu năng trên tập dữ liệu kiểm tra, cũng như phân tích kết quả hoạt 
động thực tế của toàn bộ hệ thống ScamShield AI khi kết hợp với logic lập trình và mô hình LLM Gemini.  
4.1. Môi trường thực nghiệm  
4.1.1. Cấu hình phần cứng  
Quá trình phát triển hệ thống được chia làm hai giai đoạn với cấu hình phần cứng tương ứng:  
•	Môi trường Huấn luyện (Training): Sử dụng nền tảng Google Colab Pro với GPU Tesla T4 / A100 để tăng tốc độ tính toán ma trận cho mô hình Transformer.  
•	Môi trường Triển khai (Inference): Máy tính cá nhân (Laptop) sử dụng CPU đa nhân, RAM 8GB-16GB để chạy server FastAPI nội bộ và giao diện Web.  
4.1.2. Cấu hình phần mềm và thư viện •  	Hệ điều hành: Windows 11 / macOS.  
•	Ngôn ngữ lập trình: Python (3.10+).  
•	Các thư viện chính:  
o	transformers (Hugging Face): Tải và tinh chỉnh mô hình PhoBERT.  
o 	torch (PyTorch): Framework học sâu cốt lõi. o  	fastapi, uvicorn: Xây 
	dựng API Backend và vận hành Web Server. o  	google-generativeai: Kết 
nối với API của Gemini AI.  
o	scikit-learn, numpy, pandas: Xử lý, phân chia dữ liệu và tính toán các độ đo đánh giá.  
4.2. Kết quả huấn luyện mô hình PhoBERT  
4.2.1. Phân tích đồ thị hàm mất mát (Loss Curves)  
Đồ thị hàm mất mát (Cross-Entropy Loss) thể hiện khả năng giảm thiểu sai số của mô hình trong quá trình học.  
  
Hình 6: Đồ thị hàm mất mát (Loss Curves) qua các Epochs.  
Phân tích:  
•	Xu hướng chung: Cả Training Loss và Validation Loss đều giảm mạnh ở những epoch đầu tiên, cho thấy PhoBERT đã bắt đầu nắm bắt được ngữ nghĩa và đặc trưng từ vựng của các câu lừa đảo.  
•	Hội tụ: Mô hình đạt trạng thái hội tụ tốt ở khoảng Epoch thứ 13.  
•	Overfitting: Khoảng cách giữa hai đường loss không quá lớn. Validation loss không có hiện tượng tăng vọt trở lại, chứng tỏ mô hình không bị "học vẹt" (overfitting) và có khả năng tổng quát hóa tốt trên dữ liệu văn bản mới.  
4.2.2. Phân tích đồ thị độ chính xác (Accuracy / F1-Score Curves)  
Với bài toán phân loại văn bản đa lớp (30 nhãn) và dữ liệu có thể mất cân bằng, chỉ số F1Score được theo dõi sát sao song song với Accuracy.  
   
Hình 4.2: Đồ thị độ chính xác và F1-Score qua các Epochs.  
Phân tích:  
•	Độ chính xác tăng đều đặn và đạt mức trần ở Epoch 13.  
•	Điểm nhấn của mô hình là đạt được Accuracy ~87% và F1-score lên tới 0.8387. Đối với một bài toán phân loại văn bản tiếng Việt phức tạp với 30 lớp (nhãn) khác nhau, đây là một kết quả cực kỳ ấn tượng, chứng tỏ PhoBERT đã phân tách được ranh giới ngữ nghĩa giữa các loại thủ đoạn lừa đảo tinh vi.  
4.2.3. Tóm tắt kiến trúc và số lượng tham số  
Khác với CNN, PhoBERT là một mô hình ngôn ngữ dựa trên kiến trúc Transformer (cụ thể là RoBERTa).  
•	Đầu vào: Văn bản tiếng Việt đã được phân tách từ (word segmentation).  
•	Kiến trúc lõi: 12 lớp Transformer Blocks, cơ chế Multi-head Self-Attention.  
•	Lớp đầu ra (Classification Head): Một lớp Dense (Linear) nhận vector ngữ cảnh [CLS] để xuất ra phân phối xác suất cho 30 nhãn.  
•	Tổng số tham số: ~135 triệu tham số. Khối lượng tham số đồ sộ này giúp mô hình "hiểu" được ngữ pháp tiếng Việt trước khi tinh chỉnh cho tác vụ tìm lừa đảo.  
4.3. Đánh giá hiệu năng mô hình trên tập kiểm tra (Test Set)  
4.3.1. Các độ đo tổng thể  
Trên tập dữ liệu kiểm tra (những câu tin nhắn hoàn toàn mới mà mô hình chưa từng thấy), PhoBERT đạt hiệu năng nhất quán với tập xác thực:  
•	Test Accuracy: ~87%  
•	Macro F1-Score: ~0.83 Kết quả này khẳng định mô hình đã thực sự học được bản chất của tin nhắn lừa đảo chứ không phải ghi nhớ ngẫu nhiên.  
4.3.2. Phân tích Báo cáo phân loại chi tiết (Classification Report)  
   
Hình 4.3: Báo cáo phân loại chi tiết các nhãn (Classification Report).  
Phân tích:  
•	Hiệu suất tổng thể xuất sắc: Dựa vào bảng báo cáo, có thể thấy các chỉ số Precision, Recall và F1-Score của phần lớn các nhãn đều đạt mức rất cao. Đặc biệt, nhãn 0 (Không phải lừa đảo) có độ chính xác gần như tuyệt đối với F1-score lên tới 0.97, đảm bảo hệ thống không nhận diện sai tin nhắn an toàn của người dùng.  
•	Sự nhầm lẫn nhỏ (Misclassification): Một vài nhãn có chỉ số Precision hoặc Recall thấp hơn mặt bằng chung (ví dụ: "Lừa đảo giả cơ quan nhà nước" hay "Lừa đảo giả danh công an"). Nguyên nhân là do trong thực tế, ngữ cảnh và bộ từ vựng của các thủ đoạn thao túng này rất giống nhau (đều dọa nạt, xưng danh cơ quan chức năng), ranh giới phân biệt rất mong manh ngay cả đối với con người. Tuy nhiên, AI vẫn làm rất tốt nhiệm vụ cốt lõi là phân loại chúng vào nhóm nguy hiểm.  
4.4. Kết quả hoạt động của hệ thống thời gian thực (ScamShield API)  
Để đánh giá toàn diện, nhóm không chỉ đo lường AI lõi (PhoBERT) mà còn kiểm thử toàn bộ luồng hoạt động thực tế khi kết hợp với logic Backend (Keyword Override, Biểu đồ cán cân) và Gemini AI.  
4.4.1. Kịch bản 1: Văn bản An toàn  
•	Đầu vào: "Chiều nay nhớ đi học đúng giờ nha mày."  
•	Hệ thống xử lý: PhoBERT nhận diện không có yếu tố đe dọa/dụ dỗ.  
•	Kết quả hiển thị: Giao diện web hiển thị biểu đồ đối trọng với đầy đủ hai thanh phần trăm: thanh "An toàn" (màu xanh) chiếm tỷ lệ áp đảo xếp phía trên và thanh "Nguy cơ lừa đảo" ở mức rất thấp xếp phía dưới để thể hiện sự bù trừ (tổng 100%). Hệ thống không kích hoạt Gemini AI để tối ưu hóa tốc độ phản hồi và tiết kiệm tài nguyên máy chủ.   
   
Hình 4.4: Nhận dạng văn bản giao tiếp thông thường.  
4.4.2. Kịch bản 2: Văn bản lừa đảo rõ ràng (Kích hoạt 2-Tier AI)  
•	Đầu vào: "Cơ quan CATP yêu cầu anh chuyển 5 triệu vào STK 12345 để phục vụ điều tra."  
•	Hệ thống xử lý: PhoBERT phát hiện ra nhãn "Giả danh công an" với độ tự tin cao.  
Ngay lập tức, luồng dữ liệu kích hoạt API Gemini. 

Kết quả hiển thị: Biểu đồ đối trọng hiện thanh "Lừa đảo" màu đỏ. Bên dưới, Gemini AI xuất ra đoạn văn bản phân tích chi tiết thủ đoạn thao túng tâm lý và hướng dẫn người dùng cách phòng tránh.  
 
Hình 4.5 và 4.6 : Nhận dạng lừa đảo và lời khuyên từ Gemini AI.  
4.4.3. Kịch bản 3: Kích hoạt thuật toán "Lật kèo" (Bọc lót cho AI)  
•	Đầu vào: "SIM viettel sắp khóa soạn tin... " (Câu quá ngắn, thiếu ngữ cảnh).  
Hệ thống xử lý: Ban đầu PhoBERT phân vân và có thể báo An toàn. Tuy nhiên, thuật toán Keyword Override (Quét từ khóa) chạy ngầm trên Backend phát hiện cụm từ nhạy cảm "SIM viettel", "khóa".  
•	Kết quả hiển thị: Hệ thống ngay lập tức ép (force) nhãn kết quả thành "Lừa đảo khóa SIM", đảm bảo tỷ lệ bỏ sót (False Negative) ở mức thấp nhất, đặt sự an toàn của người dùng lên hàng đầu.  
4.4.4. Trải nghiệm người dùng và Thống kê trực quan 
Bên cạnh khả năng nhận diện văn bản chính xác, hệ thống ScamShield còn cung cấp một giao diện tương tác toàn diện, tối ưu hóa trải nghiệm người dùng cuối qua các tính năng mở rộng: 
a)	Tính năng Phân tích hội thoại Tính năng này cho phép người dùng nhập hoặc dán (paste) các đoạn hội thoại dài và phức tạp. Hệ thống sẽ bóc tách và đánh giá rủi ro trên toàn bộ ngữ cảnh của cả một cuộc trò chuyện thay vì chỉ phân tích từng câu đơn lẻ. Điều này giúp người dùng nhận diện được cả một kịch bản thao túng tâm lý hoặc lừa đảo tinh vi đang diễn ra qua nhiều dòng tin nhắn. 
 
Hình 4.7: Giao diện Module phân tích ngữ cảnh hội thoại. 
b)	Module Chatbot AI (Trợ lý ảo bảo mật) Đây là một trợ lý ảo thông minh được tích hợp trực tiếp trên nền tảng. Người dùng có thể trò chuyện, đặt câu hỏi về các dấu hiệu lừa đảo mới nhất, hoặc yêu cầu Chatbot tư vấn cách xử lý khi trót bấm vào đường link lạ. Việc giao tiếp dưới dạng hỏi-đáp tự nhiên giúp hệ thống trở nên thân thiện và hỗ trợ người dùng một cách chủ động, kịp thời. 
 
Hình 4.8: Giao diện trò chuyện trực tiếp với Chatbot trợ lý ảo. 
c)	Dashboard Quản trị và Thống kê: Hệ thống cung cấp các biểu đồ thống kê trực quan về tổng số lượt quét, cũng như tỷ lệ tin nhắn an toàn/lừa đảo theo thời gian thực. Bảng điều khiển này giúp quản trị viên dễ dàng theo dõi hiệu suất hoạt động của hệ thống và nắm bắt nhanh xu hướng an ninh mạng trên nền tảng. 
 
Hình 4.9: Giao diện Dashboard thống kê tổng quan của hệ thống. 
4.4.5. Hệ thống định danh và Quản lý lịch sử cá nhân 
Để biến ScamShield AI thành một công cụ cá nhân hóa và bảo mật, hệ thống được tích hợp thêm module xác thực người dùng (Authentication) với các chức năng nổi bật: 
●	Đăng nhập và Phân quyền: Cho phép người dùng tạo tài khoản và đăng nhập an toàn. Hệ thống phân tách rõ ràng giữa phân quyền người dùng tiêu chuẩn (chỉ sử dụng tính năng quét) và Quản trị viên (được quyền truy cập vào Dashboard thống kê). 
●	Lưu trữ lịch sử phân tích: Nút chức năng "Đã lưu vào tài khoản" cho phép hệ thống tự động lưu lại các đoạn tin nhắn hoặc hình ảnh mà người dùng đã phân tích. Điều này giúp người dùng dễ dàng tra cứu lại các thủ đoạn lừa đảo đã gặp để cảnh báo cho người thân mà không cần phải quét lại từ đầu. 
 
Hình 4.10: Giao diện Đăng nhập và quản lý lịch sử phân tích cá nhân. 
  
 
 
CHƯƠNG 5. KẾT LUẬN VÀ ĐỀ XUẤT HƯỚNG PHÁT TRIỂN  
5.1. Tóm tắt các kết quả chính đạt được  
Sau quá trình nghiên cứu và phát triển, nhóm đã xây dựng thành công hệ thống ScamShield AI với các thành quả nổi bật:  
•	Huấn luyện thành công mô hình lõi: Tinh chỉnh (fine-tune) mô hình ngôn ngữ lớn PhoBERT cho tác vụ phân loại văn bản đa lớp tiếng Việt, đạt độ chính xác ~87% trên 30 nhãn dữ liệu (1 nhãn an toàn, 29 nhãn lừa đảo).  
•	Kiến trúc hệ thống 2 lớp (2-Tier AI): Kết hợp hoàn hảo giữa tốc độ phân loại siêu tốc của PhoBERT (Local Model) và khả năng lập luận, giải thích sâu sắc của Gemini AI (Cloud LLM).  
•	Thuật toán tối ưu thực tiễn: Phát triển cơ chế "Lật kèo" dựa trên bộ từ khóa để khắc phục điểm yếu của AI khi xử lý câu ngắn; Thiết kế UI biểu đồ "cán cân" tự động cân bằng tỷ lệ % rủi ro trực quan cho người dùng.  
5.2. Kết luận chung  
5.2.1. Về khả năng đáp ứng mục tiêu  
Đề tài đã hoàn thành xuất sắc các mục tiêu đặt ra ban đầu. Hệ thống hoạt động mượt mà, tốc độ phản hồi nhanh, giao diện thân thiện. Việc áp dụng mô hình Transformer kết hợp LLM chứng minh được hiệu quả vượt trội trong việc bóc tách ngữ nghĩa phức tạp của tiếng Việt so với các phương pháp học máy truyền thống (như SVM hay Naive Bayes).  
5.2.2. Về đóng góp khoa học và thực tiễn  
Khoa học: Đóng góp một "case study" (nghiên cứu trường hợp) thực tế về cách kết hợp nhiều hệ thống AI (AI tạo sinh và AI phân loại) để giải quyết một bài toán NLP đặc thù của tiếng Việt.  
•  	Thực tiễn: ScamShield AI là một công cụ có tính ứng dụng cao, có thể đưa vào sử dụng ngay để cảnh báo người dân, đặc biệt là những nhóm đối tượng yếu thế (người lớn tuổi, học sinh) trước vấn nạn lừa đảo qua mạng ngày càng tinh vi.  
5.3. Những hạn chế của đề tài  
Mặc dù đạt kết quả khả quan, hệ thống vẫn còn một số giới hạn nhất định:  
•	Sự tiến hóa của dữ liệu (Data Drift): Tội phạm mạng liên tục thay đổi kịch bản lừa đảo mỗi ngày. Nếu không được cập nhật dữ liệu huấn luyện thường xuyên, mô hình PhoBERT có thể bị lỗi thời trước các thủ đoạn hoàn toàn mới.  
•	Hạn chế trích xuất siêu dữ liệu: Hệ thống hiện tại chỉ mới dừng lại ở việc đọc hiểu "nội dung" văn bản. Nó chưa có khả năng tự động bóc tách các yếu tố kỹ thuật đi kèm tin nhắn như: Địa chỉ IP, kiểm tra độ tin cậy của đường link (URL phishing), hay định danh số điện thoại người gửi.  
5.4. Đề xuất hướng phát triển trong tương lai  
Để biến ScamShield thành một giải pháp bảo mật toàn diện, nhóm đề xuất các hướng nâng cấp sau:  
5.4.1. Nâng cấp bộ giải mã kỹ thuật (Technical Extractors)  
Sử dụng Biểu thức chính quy (Regex) và tích hợp các API kiểm tra dữ liệu tình báo mối đe dọa (Threat Intelligence) để:  
•	Tự động bóc tách và cảnh báo đường link lạ (URL) có trong tin nhắn.  
•	Kiểm tra chéo số điện thoại/số tài khoản ngân hàng trong tin nhắn với các cơ sở dữ liệu lừa đảo quốc gia.  
5.4.2. Tích hợp công nghệ Thị giác máy tính (Computer Vision)  
Phát triển tính năng nhận diện lừa đảo từ hình ảnh chụp màn hình (Screenshot). Cụ thể:  
•	Tích hợp công nghệ OCR (Optical Character Recognition) để bóc tách chữ từ ảnh chụp tin nhắn Zalo, Messenger.  
•	Tích hợp bộ giải mã mã vạch (pyzbar) để phân tích các mã QR độc hại chứa link lừa đảo bị ẩn giấu.  
5.4.3. Đóng gói và phát hành thực tế  
Nghiên cứu chuyển đổi hệ thống thành một tiện ích mở rộng trên trình duyệt (Browser Extension) hoặc một ứng dụng chạy ngầm trên điện thoại di động. Điều này giúp hệ thống tự động quét các tin nhắn SMS hoặc tin nhắn trên mạng xã hội ngay khi chúng vừa gửi đến, tạo ra một lá chắn bảo vệ chủ động theo thời gian thực.  
 
