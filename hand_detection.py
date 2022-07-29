import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)

mpHands = mp.solutions.hands
hands = mpHands.Hands(False,1)
mpDraw = mp.solutions.drawing_utils

pTime = 0
cTime = 0
i = 0
jumlah_fps = 0
while True:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = hands.process(imgRGB)
    
    if results.multi_hand_landmarks:
        for handLms in results.multi_hand_landmarks:
            mpDraw.draw_landmarks(img, handLms, mpHands.HAND_CONNECTIONS)
   
    img = cv2.flip(img,1)
    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime
    
    cv2.imshow("image", img)
    jumlah_fps += fps
    i+=1
    if cv2.waitKey(30) >= 0:
        break

print (jumlah_fps/i)
