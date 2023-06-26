# SENTINEL
SENTINEL is smart security tool that ensures the safety by detecting and recognising people who enter our property.

## METHODOLOGY
- During the initializing period we train the system with face data of familliar faces. The system saves face data of the trained models into its file directory.
- During active period the software system actively detects and tracks faces from the input source. The system captures the face data from the input.
- The system used advanced face detection and recognition models and libraries from OpenCV and simillar libraries to recognize the face data from the input.
- It uses the face data collected from input to check with already saved face data in the database.
- If the face is recognized the system raises no alert. And the person can pass without suspesion. But, if the system doesn't recognize the face alerts the user of the unrecognized entry with captured face data, and actively tracks the detected face.
- If the system further detects suspesious activity it further gives an option to forward the alert the local law.

## NECESSARY PACKAGES AND MODULES

- tkinter
- turtle
- cv2
- os
- subprocess
- numpy
- twilio

## IMPLEMENTATION STEPS

- Extracting face data from the Known faces directory.
- Capturing, resizing and enhancing faces through the video source.
- Comparing the captured face with existing face data present in the directory.
- Updating intruder data in the CSV file and send user alert using twilio API if an intruder is detected.

## EXPLAINATION

- In this code we're utilising already existing openCV modules for advanced face recognition.
- The code allows us to modify and add more users to our liking so that they aren't categorized as intruders anymore.
- We're implementing a third-party API known as twilio to send appropriate messages to our mobile number when an intruder is detected, an image of the intruder is also saved in the system along with that hence enabling us to monitor our house and go out tension free.
- In the credentials.txt file give information about your twilio account and your number so that the program can link your twilio account registered by your phone number.
- The current system is limited by many factors, it lacks a dedicated server or a database and is very much hardware dependent and it has a lot of scope for improvement.

## SCREENSHOTS

![image](https://github.com/TH4Mpuran/SENTINEL/assets/93757313/4dd84629-a683-44d4-bbf6-22e2e2c0887d)


![image](https://github.com/TH4Mpuran/SENTINEL/assets/93757313/7dc0ad1e-eed0-42a5-94fd-9c01e322b8b3)

# Thank You

  




