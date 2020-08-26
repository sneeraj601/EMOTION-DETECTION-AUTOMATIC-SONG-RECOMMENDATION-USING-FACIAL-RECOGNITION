# EMOTION-DETECTION-AUTOMATIC-SONG-RECOMMENDATION-USING-FACIAL-RECOGNITION
This project detects the expression of the person and play a song according to the mood.
Start with python script : python guibg.py
Overview :
Automated facial expression recognition is a task in computer vision and robotics. Facial expressions play an important role in recognition of emotions and are used in the process of non-verbal communication, as well as to identify people. They are very important in daily emotional communication, just next to the tone of voice.

Description :
This application detects the emotion of the user and plays a song according to the expression so that the user can feel better and can get the better mood.. The system consists of a camera that captures the images of the person and sends it to the image enhancement module i.e for preprocessing. After preprocessing the image comes in the Face Detection phase where face is detected from the images that are captured real time and after the detection phase emotion classification phase starts and result in detected emotion of the person. After detecting the mood a song is played according to the emotion.

Dataset :
This application involves the dataset used for implementing the FER system was the FER2013 dataset from the Kaggle challenge on FER (Goodfellow et al., 2013). The dataset consists of 35,887 labelled images, which are divided into 3589 test and 28709 train images. The dataset consists of another 3589 private test images, on which the final test was conducted during the challenge.

Dependencies:
Tkinter
Os
Subprocess
OpenCv
Time
Keras
Numpy
Tensorflow
Pygame
Playsound
Pyttsx3
Threading
Sys
Random
