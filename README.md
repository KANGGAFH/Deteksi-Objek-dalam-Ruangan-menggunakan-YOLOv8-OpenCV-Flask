# 🧠 Deteksi Orang dalam Ruangan menggunakan YOLOv8, OpenCV & Flask

Aplikasi web sederhana yang memungkinkan deteksi keberadaan **orang** dalam gambar, video, dan kamera real-time menggunakan **YOLOv8**, **OpenCV**, dan **Flask**.

---

## 🎯 Fitur

✅ Upload gambar dan video untuk dideteksi  
✅ Deteksi orang secara real-time dari kamera laptop/server  
✅ Tampilkan jumlah orang yang terdeteksi  
✅ Tampilan web responsif dan modern (Bootstrap 5)  
✅ Bisa diakses dari jaringan lokal (LAN)

---

## 🧑‍💻 Teknologi yang Digunakan

| Komponen       | Teknologi                     |
|----------------|-------------------------------|
| Backend        | Python 3 + Flask              |
| Deteksi AI     | YOLOv8 (via Ultralytics)      |
| Pengolahan Citra | OpenCV, NumPy               |
| Tampilan Web   | HTML, Bootstrap, Jinja2       |

---

📂 Struktur Folder
```csharp
├── app.py
├── templates/
│   ├── base.html
│   ├── index.html
│   └── result.html
├── static/
│   └── style.css
├── uploads/                ← Menyimpan hasil deteksi
├── utils/
│   └── detector.py         ← Deteksi YOLOv8
└── requirements.txt
```

---

## 🚀 Cara Menjalankan Proyek

### 📦 1. Clone Repo
```bash
git clone https://github.com/KANGGAFH/Deteksi-Objek-dalam-Ruangan-menggunakan-YOLOv8-OpenCV-Flask.git
cd Deteksi-Objek-dalam-Ruangan-menggunakan-YOLOv8-OpenCV-Flask
```

### 📥 2. Install Semua Dependency
```bash
pip install -r requirements.txt
```

### 🧠 3. Download Model YOLOv8
jalankan python:
```python
from ultralytics import YOLO
YOLO("yolov8n.pt")
```
Model ini akan otomatis disimpan dan digunakan untuk deteksi objek.

### 🟢 5. Jalankan Aplikasi
```bash
python app.py
```
Nantinya akan muncul:
```csharp
 * Running on http://127.0.0.1:5000
 * Running on http://<IP_KOMPUTER_KAMU>:5000
```

### 🌐 6. Akses dari Browser
- Lokal:
  ```arduino
  http://localhost:5000
  ```
- Perangkat Lain (masih satu jaringan)
  ```cpp
  http://<IP_KOMPUTER_KAMU>:5000
  ```
Cek IP lokal dengan:
```bash
ipconfig  # Windows
ifconfig  # Linux/macOS
```



