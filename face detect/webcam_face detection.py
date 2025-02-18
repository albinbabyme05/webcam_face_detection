import cv2
import time

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Using a webcam
cam = cv2.VideoCapture(0)

# Set frame dimensions and adjust brightness
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height
cam.set(10, 100) # Brightness

img_counter = 0
start_time = 0

while True:
    ret, frame = cam.read()
    faces = face_cascade.detectMultiScale(frame, 1.1, 4)

    # Calculate FPS
    current_time = time.time()
    fps = 1 / (current_time - start_time)
    start_time = current_time

    for (x, y, width, height) in faces:
        cv2.rectangle(frame, (x, y), (x + width, y + height), (0, 255, 0), 2)

    # Display FPS on the video feed
    cv2.putText(frame, f"FPS: {int(fps)}", (520, 40), cv2.FONT_HERSHEY_PLAIN, 1.1, (255, 255, 0), 3)

    cv2.imshow("Video", frame)

    key = cv2.waitKey(10) % 256

    if key == 27:  # Escape key to exit
        print('Escape pressed. Closing the application')
        break
    elif key == 32:  # Space key to save frame
        img_location = f"C:/Users/user/Pictures/Camera Roll/opencv_frame_{img_counter}.png"
        cv2.imwrite(img_location, frame)
        print(f"{img_location} saved")
        img_counter += 1

cam.release()
cv2.destroyAllWindows()
