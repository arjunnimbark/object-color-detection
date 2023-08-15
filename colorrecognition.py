import cv2 as cv
import numpy as np

#accessing webcam
cap=cv.VideoCapture(0);

#set the height and width
cap.set(cv.CAP_PROP_FRAME_HEIGHT,720)
cap.set(cv.CAP_PROP_FRAME_WIDTH,1280)

while True:
    _, frame=cap.read()
    
    hsv_frame=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    height,width,_=frame.shape
    
    #finding median of the frame
    cx=int(width/2)
    cy=int(height/2)
    
    pixel_center=hsv_frame[cy,cx]
    hue_value=pixel_center[0]
    
    #putting color ranges
    color = "Undefined"
    if hue_value < 5:
        color = "RED"
    elif hue_value < 22:
        color = "ORANGE"
    elif hue_value < 33:
        color = "YELLOW"
    elif hue_value < 78:
        color = "GREEN"
    elif hue_value < 131:
        color = "BLUE"
    elif hue_value < 170:
        color = "VIOLET"
    else:
        color = "RED"
    
    #providing color
    pixel_bgr=frame[cy,cx]
    b,g,r=int(pixel_bgr[0]),int(pixel_bgr[1]),int(pixel_bgr[2])
    
    #cv.rectangle(frame, (cx - 220, 10), (cx + 200, 120), (255, 255, 255), -1)
    cv.putText(frame, color, (cx - 200, 100), 0, 3, (b, g, r), 3)
    cv.circle(frame, (cx, cy), 5, (25, 25, 25), 3)
    cv.imshow("Frame", frame)
    key = cv.waitKey(1)
    if key == 27:
        break
    
cap.release()
cv.destroyAllWindows()
