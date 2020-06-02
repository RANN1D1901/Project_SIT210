# Project_SIT210
File description:faceDetection.py: Code to detect faces using OpenCV and HaarCascade XML File.
faceRecognition.py: Code to train a machine learning model to recognise the face by feeding the training data(users images) to the algorithm.
final.py: The code that monitors the working of the embedded system.
haarcascade_frontalface_default.xml: XML file used to detect faces in the video, this video has numerous photos stored in form of arrays and
the when detecting the faces this file is used to read and detect the face of the person.
mqtt.ino: The code uploaded to argon to receive signal from the raspberry pi once the motion is detected in the premises.
prepare dataset.py: Code to click images of the face of the user which needs to be detected by the machine learning algorithm.
i2cArduino: Code upoloaded on arduino to read data from raspberry pi to switch the light the premises on.
