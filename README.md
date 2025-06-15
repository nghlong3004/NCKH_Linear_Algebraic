# 🇻🇳 **MỘT SỐ BÀI TOÁN THỰC TẾ CỦA MA TRẬN, ĐỊNH THỨC VÀ HỆ PHƯƠNG TRÌNH TUYẾN TÍNH**
> *Undergraduate Research Project – Hanoi University of Mining and Geology (HUMG), 05 / 2025*

<p align="center">
  <img src="https://user-images.githubusercontent.com/placeholder-university-logo.png" alt="HUMG" width="120"/>
</p>

<p align="center">
  <a href="LICENSE"><img src="https://img.shields.io/badge/license-MIT-green.svg" alt="License"/></a>
  <img src="https://img.shields.io/badge/python-3.10%2B-blue" alt="Python"/>
  <img src="https://img.shields.io/badge/build-passing-brightgreen" alt="Build"/>
</p>

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

## Mục lục
- [Tổng quan](#-tổng-quan)
- [Cấu trúc](#-cấu-trúc)
- [Thiết lập nhanh](#️-thiết-lập-nhanh)
- [Sử dụng](#-sử-dụng)
- [requirements.txt có gì?](#-requirementstxt-có-gì)
- [Tác giả](#-tác-giả)

---

## 📁 Cấu trúc
```text
.
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
├── requirements.txt          # include python
└── README.md                 # (tài liệu này)
```
---

## Thiết lập nhanh
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
| `PageRank.py` | Tính xếp hạng PageRank cho đồ thị nhỏ | `python src/PageRank.py` |
| `SiMplexAlgorithm.py` | Giải **Linear Programming** bằng phương pháp Simplex | `python src/SiMplexAlgorithm.py` |

> Scripts ghi log ra console & file `log/output.log` (tùy cấu hình).

---

## Tác giả

| Vai trò | Họ tên | Lớp |
|---------|--------|-----|
| **Trưởng nhóm** | Nguyễn Hoàng Long | DCCDTD68B |
| Thành viên | Nguyễn Đại Lực | DCCTCT68A |
|  | Vũ Ngọc Linh | DCCBHD69 |
|  | Nguyễn Cao Thanh Huyền | DCCBHD69 |
| **GV Hướng dẫn** | GVC.TS Lê Bích Phượng | Bộ môn Toán – HUMG |

Liên hệ: **nghlong3004@gmail.com**

---

<p align="center">💡 *“Mathematics is the language with which God has written the universe.”* — Galileo Galilei</p>
