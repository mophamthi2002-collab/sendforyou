# Website thiệp tình yêu (Python Flask)

## 1. Cài đặt
Mở thư mục dự án bằng Visual Studio Code. Mở Terminal và chạy:

```bash
python -m venv venv
```

Kích hoạt môi trường ảo:

- Windows: `venv\Scripts\activate`
- macOS/Linux: `source venv/bin/activate`

Cài thư viện:

```bash
pip install -r requirements.txt
```

## 2. Chạy website

```bash
python app.py
```

Mở trình duyệt tại: http://127.0.0.1:5000

## 3. Tùy chỉnh nội dung và ảnh

- Trang đầu: sửa `templates/index.html`.
- Nội dung lá thư: sửa phần chữ trong `templates/letter.html`.
- Ảnh: thay các file trong `static/images/`.

Để thay ảnh của bạn, hãy giữ tên `photo1.svg`, `photo2.svg`, `photo3.svg` nếu dùng SVG; hoặc đổi đuôi và sửa đường dẫn `src` trong `letter.html` cho đúng, ví dụ `photo1.jpg`.

## Cấu trúc thư mục

```text
thiep_tinh_yeu/
├── app.py
├── requirements.txt
├── README.md
├── templates/
│   ├── index.html
│   └── letter.html
└── static/
    ├── style.css
    └── images/
        ├── photo1.svg
        ├── photo2.svg
        └── photo3.svg
```
