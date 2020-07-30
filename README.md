# Face-recognition:
Face recognition is a method of identifying or verifying the identity of an individual using their face. Face recognition systems can be used to identify people in photos, video, or in real-time

## Packages required:
(a) opencv : It is a library of programming functions mainly aimed at real-time computer vision.

## About the haarcascade file:
In this project we will be using the haarcascade_frontalface_default.xml which is a haar cascade designed by OpenCV to detect the frontal face. This haar cascade is available on github. A Haar Cascade works by training the cascade on thousands of negative images with the positive image superimposed on it.

![p](https://user-images.githubusercontent.com/68856803/88895856-a67e1780-d266-11ea-8f70-88e1ae3223b7.png)

## Steps to build this project
(a) Import the required libraries

(b) Include the haarcascade_frontalface_default.xml

(c)  Open the inbuilt Camera

(d) Now we will capture the frames from the camera

(e) Get the gray scaled image

(f) Draw a rectangle around the faces

(g) Display the resulting frame i.e, the output

(h) When everything is done, release the capture

## Execution:
run the program by using the following command:

-> python face_rec.py
