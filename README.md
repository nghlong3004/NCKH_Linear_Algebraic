# **MỘT SỐ BÀI TOÁN THỰC TẾ CỦA MA TRẬN, ĐỊNH THỨC VÀ HỆ PHƯƠNG TRÌNH TUYẾN TÍNH**
> *Undergraduate Research Project – Hanoi University of Mining and Geology (HUMG), 05 / 2025*

---

## Tổng quan
Kho lưu trữ này đính kèm **báo cáo PDF**, mã nguồn **Python**, tài liệu tham khảo và slide phục vụ đề tài nghiên cứu sinh viên:

> **Mục tiêu:** Hệ thống hóa lý thuyết đại số tuyến tính & minh chứng **4 nhóm ứng dụng trọng yếu**:
>
> 1. **Tối ưu hóa tuyến tính** (Linear Programming)  
> 2. **Mã hóa Hill** (Hill Cipher)  
> 3. **Thuật toán PageRank**  
> 4. **Chuỗi Markov**
>
> Mỗi chủ đề kèm mô tả toán học, code Python và hình ảnh trực quan.

---
### Thành tích & Công bố
| Mô tả | Thông tin |
|-------|-----------|
| **Giải thưởng** | **Giải Nhì Nghiên cứu Khoa học sinh viên** – HUMG 2025 (T13) |
| **Bài báo** | **Lê Bích Phượng & Nguyễn Hoàng Long** (2025). *Phát triển năng lực giải quyết vấn đề cho sinh viên Trường Đại học Mỏ – Địa chất thông qua giảng dạy môn Đại số tuyến tính / Developing problem‑solving skills for students at HUMG through teaching Linear Algebra.* **Tạp chí Giáo dục & Xã hội (Journal of Education and Society)**, Số 166 (227), tháng 1/2025 (kì 1), ISSN 1859‑3917, trang 53‑60. |

---

## Mục lục
- [Tổng quan](#-Tổng-quan)
- [Thành tích & Công bố](#-thành-tích--công-bố)
- [Cấu trúc](#-cấu-trúc)
- [Cài đặt](#️-cài-đặt)
- [Sử dụng](#-sử-dụng)
- [Tác giả](#-tác-giả)

---

## Cấu trúc
```text
├── docs/                     # Báo cáo & slide & bài báo tạp trí
│   ├── Bao_cao_NCKH_NguyenHoangLong.pdf
│   ├── TomTatBaoCao.pdf
│   ├── magazine.pdf
│   └── slide_NCKH_NguyenHoangLong.pdf
├── notebooks/                # Tài liệu tham khảo (PDF)
│   ├── Elementary-Linear-Algebra-Applications.pdf
│   ├── LA-app1.pdf
│   ├── Theory_Linear_Algebra.pdf
│   └── linear-algebra-with-applications.pdf
├── src/                      # Python
│   ├── HillCipher.py
│   ├── PageRank.py
│   └── SiMplexAlgorithm.py
├── requirements.txt 
└── README.md 
```
---

## Cài đặt
```bash
# Clone repo
git clone https://github.com/nghlong3004/applications-linear-algebraic.git
cd applications-linear-algebraic

# instal requirements.txt
pip install -r requirements.txt

# example script
python src/PageRank.py
```

---

## Sử dụng

| Script | Mục đích | Cách chạy nhanh |
|--------|----------|-----------------|
| `HillCipher.py` | Mã hóa / giải mã văn bản bằng **Hill Cipher** | `python src/HillCipher.py --help` |
| `PageRank.py` | Tính xếp hạng PageRank | `python src/PageRank.py` |
| `SiMplexAlgorithm.py` | Giải **Linear Programming** bằng phương pháp Simplex | `python src/SiMplexAlgorithm.py` |

> Scripts ghi log ra console & file `log/output.log` (tùy cấu hình).

---

## 👥 Tác giả
| Vai trò | Họ tên | Đơn vị |
|---------|--------|--------|
| **Trưởng nhóm** | Nguyễn Hoàng Long | Khoa Cơ điện – HUMG |
| **GV Hướng dẫn** | GVC.TS Lê Bích Phượng | Khoa Khoa học Cơ bản – HUMG |

*Các thành viên cộng tác được ghi nhận trong báo cáo dạng PDF.*

Liên hệ: **nghlong3004@gmail.com**

---

<p align="center">*“Mathematics is the language with which God has written the universe.”* — Galileo Galilei</p>
