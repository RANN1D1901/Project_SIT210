Sending Signal/Data through cloud:
1)	On particle IDE upload file mqtt.ino, this is where we set our cloud environment to receive any signal or data from raspberry pi.
2)	This is necessary to execute the function MQTT() in our final.py file because this is where we subscribe to any signal sent through our system which is published in function MQTT().
3)	This is also necessary to create an IFTTT trigger as this is where we use Particle.Variable() method to change intruder variable 1, indication of motion in the premises in context of embedded system.
Communication Between Arduino and Raspberry Pi:
1)	After completing step 1, the slave/master relationship has to be established between Arduino and raspberry pi so that we are able to perform some automation inside the premises itself.
2)	To do this connect Arduino to your computer and upload i2cArduino.ino file to Arduino, this would make Arduino a slave and would enable it to switch the led on or off, depending upon the signal sent from master (Raspberry Pi in our case).
3)	It is necessary for execution of LIGHT() function of final.py code where we are controlling the led of premises based on different scenarios.

Machine Learning to Recognise Faces:

1)	This was a long process and these steps must be completed even before writing final script that is final.py.
2)	The first step necessary to make a face recogniser is to download the file which stores numerous samples of faces in form of negative and positive images ,link : https://github.com/RANN1D1901/Project_SIT210/blob/master/haarcascade_frontalface_default.xml.
3)	The second step is to start detection of faces in order to know whether the file we downloaded works correctly and the faces are read or not, link to code: https://github.com/RANN1D1901/Project_SIT210/blob/master/faceDetection.py, make sure to change the file directory according to what exits in your pc.
4)	The next step is to prepare dataset of images of our face, this is done by clicking images of the faces detected by raspberry pi camera itself, link to code: https://github.com/RANN1D1901/Project_SIT210/blob/master/prepare%20dataset.py, again take care of the directory of file dataset.
5)	After we are finished creating dataset, a model has to be trained which recognises our face and labels it accordingly, this can be done with code in link: https://github.com/RANN1D1901/Project_SIT210/blob/master/faceRecognition.py, this piece of code assigns labels to our name and saves this to main haarcascade_frontalface_default.xml with labels against our images, necessary when trying to recognise the face detected in the video.
6)	All these steps are pre-requisites to run function DETECTION() in final.py file, therefore all 5 steps should be taken before implementation of final script.

Conclusion:
After executing all the files directed in this document, make the connections shown in circuit diagram and run the final.py code on raspberry pi and the system would start working.

