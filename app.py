from flask import Flask, render_template, request, redirect, url_for, send_from_directory, Response
import os
import cv2
from utils.detector import deteksi_frame
from werkzeug.utils import secure_filename

UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'mp4'}

app = Flask(__name__)
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

kamera_on = False

# Fungsi untuk cek ekstensi file
def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Beranda
@app.route('/')
def index():
    return render_template('index.html')

# Route untuk upload gambar/video
@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return redirect(url_for('index'))
    
    file = request.files['file']
    
    if file and allowed_file(file.filename):
        filename = secure_filename(file.filename)
        filepath = os.path.join(app.config['UPLOAD_FOLDER'], filename)
        file.save(filepath)

        # Panggil fungsi deteksi orang dari utils
        from utils.detector import deteksi_orang
        hasil_path, jumlah_orang = deteksi_orang(filepath)

        if not hasil_path:
            return "Gagal memproses file. Format tidak didukung atau error saat deteksi.", 400

        filename_only = os.path.basename(hasil_path)
        return render_template('result.html', hasil=filename_only, jumlah=jumlah_orang)

    return redirect(url_for('index'))

# Route halaman kamera
@app.route('/kamera')
def kamera():
    return render_template('kamera.html')

# Stream video ke browser
def gen_frames():
    global kamera_on
    kamera_on = True  # aktifkan kamera saat stream dimulai

    cap = cv2.VideoCapture(0)
    while kamera_on:
        success, frame = cap.read()
        if not success:
            break
        frame = deteksi_frame(frame)
        _, buffer = cv2.imencode('.jpg', frame)
        frame_bytes = buffer.tobytes()
        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')
    cap.release()  # kamera dimatikan di sini


# Route kamera stop
@app.route('/kamera/stop')
def stop_kamera():
    global kamera_on
    kamera_on = False
    return redirect(url_for('index'))


# Route untuk stream kamera
@app.route('/video_feed')
def video_feed():
    return Response(gen_frames(), mimetype='multipart/x-mixed-replace; boundary=frame')

# Menampilkan file hasil
@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

@app.route('/uploads/<path:filename>')
def uploaded_file_any(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

