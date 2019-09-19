import cv2
import matplotlib.pyplot as plt
import dlib
from imutils import face_utils

font = cv2.FONT_HERSHEY_SIMPLEX
cascPath = "/anaconda3/envs/real-python/lib/python3.7/site-packages/cv2/data/haarcascade_frontalface_default.xml"
eyePath = "/anaconda3/envs/real-python/lib/python3.7/site-packages/cv2/data/haarcascade_eye.xml"
smilePath = "/anaconda3/envs/real-python/lib/python3.7/site-packages/cv2/data/haarcascade_smile.xml"

faceCascade = cv2.CascadeClassifier(cascPath)
eyeCascade = cv2.CascadeClassifier(eyePath)
smileCascade = cv2.CascadeClassifier(smilePath)

gray = cv2.imread('../data/face.png', 0)
plt.figure(figsize=(12, 8))
plt.imshow(gray, cmap='gray')
plt.show()

faces = faceCascade.detectMultiScale(
    gray,
    scaleFactor=1.1,
    minNeighbors=5,
    flags=cv2.CASCADE_SCALE_IMAGE
)

for (x, y, w, h) in faces:
    cv2.rectangle(gray, (x, y), (x+w, y+h), (255, 255, 255, 255), 3)

plt.figure(figsize=(12, 8))
plt.imshow(gray, cmap='gray')
plt.show()

