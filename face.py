import cv2
import face_recognition
from flask import Flask, render_template, Response

app = Flask(__name__)

# Détecter les visages dans une image
def detect_faces_in_image(file_stream):
    image = face_recognition.load_image_file(file_stream)
    face_locations = face_recognition.face_locations(image)
    return len(face_locations) > 0

# Page d'accueil
@app.route('/')
def index():
    return render_template('index.html')

# Route pour le flux vidéo de la caméra
def video_feed():
    camera = cv2.VideoCapture(0)
    while True:
        success, frame = camera.read()
        if not success:
            break

        # Détecter les visages dans le frame
        rgb_frame = frame[:, :, ::-1]
        face_locations = face_recognition.face_locations(rgb_frame)

        # Dessiner un rectangle autour des visages détectés
        for (top, right, bottom, left) in face_locations:
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        ret, jpeg = cv2.imencode('.jpg', frame)
        frame_bytes = jpeg.tobytes()

        yield (b'--frame\r\n'
               b'Content-Type: image/jpeg\r\n\r\n' + frame_bytes + b'\r\n')

    camera.release()

@app.route('/video_feed')
def video_feed_route():
    return Response(video_feed(),
                    mimetype='multipart/x-mixed-replace; boundary=frame')

if __name__ == '__main__':
    app.run(debug=True)

