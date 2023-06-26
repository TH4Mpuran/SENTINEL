import cv2
import numpy as np
import face_recognition
import os,sys
import time
from datetime import datetime
from twilio.rest import Client

with open('credentials.txt','r') as myfile:
  cred_data = myfile.read()
infot = eval(cred_data)


current_dir=os.path.dirname(os.path.abspath(__file__))
path = os.path.join(current_dir, "knownFaces")

last_execution_time = 0
images = []
classNames = []
face_locations = []
myList = os.listdir(path)

for cl in myList:
    curImg = cv2.imread(f'{path}/{cl}')
    images.append(curImg)
    classNames.append(os.path.splitext(cl)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)
        encode = face_recognition.face_encodings(img)[0]
        encodeList.append(encode)
    return encodeList

def markTime(name):
    with open('timestamps.csv','r+') as f:
        myDataList = f.readlines()
        nameList = []
        for line in myDataList:
            entry = line.split(',')
            nameList.append(entry[0])
            now=datetime.now()
            dtString=now.strftime('%H:%M:%S')
            f.writelines(f'\n{name},{dtString}')

def sentMsg(infot):
    account_sid = infot['account_sid']
    auth_token = infot['auth_token']

    now = datetime.now()
    dtString = now.strftime('%H:%M:%S')
    client = Client(account_sid, auth_token)
    message = client.messages.create(to=infot['your_num'],
                                     from_=infot['trial_num'],
                                     body="Sentinel:Intruder Alert at {}.".format(dtString))

def ss():
    entry_time = datetime.now().strftime("%A, %I-%M-%S %p %d %B %Y")
    file_name = 'outputs/{}.jpg'.format(entry_time)

    cv2.imwrite(file_name,img)
    print("Frame captured and saved as:", file_name)



encodeListKnown = findEncodings(images)
print('Encoding complete')

cap = cv2.VideoCapture(0)

if not cap.isOpened():
    sys.exit('Video source not found...')

while True:
    success, img = cap.read()
    imgS = cv2.resize(img, (0, 0), None, 0.25, 0.25)
    imgS = cv2.cvtColor(imgS, cv2.COLOR_BGR2RGB)

    facesCurFrame = face_recognition.face_locations(imgS)
    encodesCurFrame = face_recognition.face_encodings(imgS, facesCurFrame)


    for encodeFace, faceLoc in zip(encodesCurFrame, facesCurFrame):
        matches = face_recognition.compare_faces(encodeListKnown, encodeFace)
        faceDis = face_recognition.face_distance(encodeListKnown, encodeFace)
        print(faceDis)
        matchIndex = np.argmin(faceDis)

        if faceDis[matchIndex] < 0.6:
            name = classNames[matchIndex].upper()
            print(name)

        else:
            name = 'Unknown'

            current_time = time.time()
            if current_time - last_execution_time >=5:

                #markTime()
                #sentMsg(infot)
                ss()
                last_execution_time = current_time

        y1, x2, y2, x1 = faceLoc

        y1, x2, y2, x1 = y1 * 4, x2 * 4, y2 * 4, x1 * 4

        cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 2)
        cv2.rectangle(img, (x1, y2 - 35), (x2, y2), (0, 0, 255), cv2.FILLED)
        cv2.putText(img, name,(x1 + 6, y2 - 6), cv2.FONT_HERSHEY_DUPLEX, 0.8, (255, 255, 255), 1)



    cv2.imshow('Input', img)
    if cv2.waitKey(1) == ord('o'):
        break



cap.release()
cv2.destroyAllWindows()
