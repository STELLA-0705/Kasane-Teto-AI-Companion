import cv2


camera = cv2.VideoCapture(0)

face_detector = cv2.CascadeClassifier(
    cv2.data.haarcascades +
    "haarcascade_frontalface_default.xml"
)


def see():

    ret, frame = camera.read()

    if not ret:
        return False


    gray = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2GRAY
    )


    faces = face_detector.detectMultiScale(
        gray,
        1.3,
        5
    )


    if len(faces) > 0:
        return True

    return False