
import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')


import cv2

# Load the pre-trained face detection model
face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_default.xml')

# Using a webcam
cam = cv2.VideoCapture(0)

# Set frame dimensions and adjust brightness
cam.set(3, 640)  # Width
cam.set(4, 480)  # Height
cam.set(10, 100) # Brightness
