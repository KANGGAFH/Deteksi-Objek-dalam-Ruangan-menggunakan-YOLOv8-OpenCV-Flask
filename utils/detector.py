# utils/detector.py
import os
import cv2
from ultralytics import YOLO

# Load model YOLOv8 (pre-trained)
model = YOLO("yolov8n.pt")  # pastikan model sudah didownload

def deteksi_orang(filepath):
    filename = os.path.basename(filepath)

    # Baca gambar / video
    if filename.lower().endswith(('.png', '.jpg', '.jpeg')):
        hasil_path, jumlah_orang = proses_gambar(filepath)
    elif filename.lower().endswith('.mp4'):
        hasil_path, jumlah_orang = proses_video(filepath)
    else:
        return None, 0

    return hasil_path, jumlah_orang

def proses_gambar(path):
    hasil = model(path)[0]

    # Hanya deteksi class 0 (orang)
    hasil_boxes = [box for box in hasil.boxes if int(box.cls[0]) == 0]

    jumlah_orang = len(hasil_boxes)
    hasil_img = hasil.plot()  # Visualisasi bounding box

    nama_hasil = "hasil_" + os.path.basename(path)
    path_hasil = os.path.join("uploads", nama_hasil)
    cv2.imwrite(path_hasil, hasil_img)

    return path_hasil, jumlah_orang

def proses_video(path):
    cap = cv2.VideoCapture(path)
    nama_hasil = "hasil_" + os.path.basename(path)
    out_path = os.path.join("uploads", nama_hasil)

    fourcc = cv2.VideoWriter_fourcc(*'mp4v')
    fps = cap.get(cv2.CAP_PROP_FPS)
    width  = int(cap.get(cv2.CAP_PROP_FRAME_WIDTH))
    height = int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))

    out = cv2.VideoWriter(out_path, fourcc, fps, (width, height))
    jumlah_orang_total = 0

    while True:
        ret, frame = cap.read()
        if not ret:
            break
        hasil = model(frame)[0]
        hasil_boxes = [box for box in hasil.boxes if int(box.cls[0]) == 0]
        jumlah_orang_total += len(hasil_boxes)
        out.write(hasil.plot())

    cap.release()
    out.release()

    return out_path, jumlah_orang_total

def deteksi_frame(frame):
    hasil = model(frame)[0]
    hasil_boxes = [box for box in hasil.boxes if int(box.cls[0]) == 0]
    return hasil.plot()

