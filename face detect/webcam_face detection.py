import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Using a webcam
cam = cv2.VideoCapture(0)

# Set frame dimensions and adjust brightness
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height
cam.set(10, 100) # Brightness

while True:
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    cv2.imshow("Video", frame)

    if cv2.waitKey(10) % 256 == 27:  # Escape key to exit
        print('Escape pressed. Closing the application')
        break

cam.release()
cv2.destroyAllWindows()
