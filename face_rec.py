import cv2
import os

face_Cascade=cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
cap=cv2.VideoCapture(0)

while True:
    # Capture frame-by-frame
    ret, img=cap.read()
    img_gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    faces=face_Cascade.detectMultiScale(img_gray,scaleFactor=1.1,minNeighbors=5)

    # Draw a rectangle around the faces
    for (x, y, w, h) in faces:
        cv2.rectangle(img,(x,y),(x+w, y+h),(255,0,0), 2)

    # Display the resulting frame
    cv2.imshow('Video',img)

    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

# When everything is done, release the capture
cap.release()
cv2.destroyAllWindows()