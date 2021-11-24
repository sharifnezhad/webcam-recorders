
import numpy as np
import cv2 
import keyboard

cap = cv2.VideoCapture(0)
cap.set(3,640)
cap.set(4,480)

fourcc = cv2.VideoWriter_fourcc(*'MP4V')
out = cv2.VideoWriter('output.mp4', fourcc, 20.0, (640,480))
font = cv2.FONT_HERSHEY_COMPLEX
menu_text='exit-->q'
y0, dy = 50, 4
y = y0 * dy*7
while(True):
    ret, frame = cap.read()
    cv2.putText(frame, menu_text, (10, 50),font, 0.5, (0,0,0), 1, cv2.LINE_AA)
    out.write(frame)
    cv2.imshow('frame', frame)
    c = cv2.waitKey(1)
    if keyboard.is_pressed('q'):
        break

# cap.release()
# out.release()
cv2.destroyAllWindows()