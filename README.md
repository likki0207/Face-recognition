# Face-recognition
OpenCV is a library of programming functions mainly aimed at real-time computer vision.

To build our face recognition system, we’ll first perform face detection, 
extract face embeddings from each face using deep learning, 
train a face recognition model on the embeddings, 
and then finally recognize faces in both images and video streams with OpenCV.

While we used OpenCV to facilitate face recognition, OpenCV itself was not responsible 
for identifying faces.

* First we need to install all the required libraries:
  make sure that you are in the correct directory;
  type the command:
  (1) pip install -r requirements.txt

* Then you need to run the program by using the following command:
  (2) python face_rec.py

* We have saved the pictures of few known personalities. If the test image contains the
  image of them, then the name will be displyed along with the square around their face; 
  Else 'unknown' will be seen along with the square around their face 
