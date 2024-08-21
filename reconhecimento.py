import face_recognition
import cv2

def capture_face():
    video_capture = cv2.VideoCapture(0)
    ret, frame = video_capture.read()
    video_capture.release()
    if not ret:
        raise Exception("Não foi possível capturar a imagem.")
    face_locations = face_recognition.face_locations(frame)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    return face_encodings

def recognize_face(encoding_to_check, known_face_encodings):
    matches = face_recognition.compare_faces(known_face_encodings, encoding_to_check)
    return True in matches
