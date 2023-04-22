import numpy as np
import cv2
import serial 
import time
import math


ser= serial.Serial('COM13', 9600)
  
shoot = '0'
ty = 1
tx = 1
# Capturing video through webcam
webcam = cv2.VideoCapture(1)
  
# Start a while loop
while(1):
      
    # Reading the video from the
    # webcam in image frames
    _, imageFrame = webcam.read()
  
    # Convert the imageFrame in 
    # BGR(RGB color space) to 
    # HSV(hue-saturation-value)
    # color space
    hsvFrame = cv2.cvtColor(imageFrame, cv2.COLOR_BGR2HSV)
  
    color_lower = np.array([101,50,38])
    color_upper = np.array([110,255,255])
    color_mask = cv2.inRange(hsvFrame, color_lower, color_upper)
      
    # Morphological Transform, Dilation
    # for each color and bitwise_and operator
    # between imageFrame and mask determines
    # to detect only that particular color
    kernel = np.ones((5, 5), "uint8")
    

    color_mask = cv2.dilate(color_mask, kernel)
    res_color = cv2.bitwise_and(imageFrame, imageFrame,
                               mask = color_mask)
    
    contours, hierarchy = cv2.findContours(color_mask,
                                           cv2.RETR_TREE,
                                           cv2.CHAIN_APPROX_SIMPLE)
    
    for pic, contour in enumerate(contours):
        area = cv2.contourArea(contour)
        if(area > 500):
            x, y, w, h = cv2.boundingRect(contour)
            imageFrame = cv2.rectangle(imageFrame, (x, y),
                                       (x + w, y + h),
                                       (0, 0, 0), 2)
            tx=x+math.floor(w/2)
            ty=y+math.floor((7*h)/20)
            shoot = '1'
              
            cv2.putText(imageFrame, "Colour", (x, y),
                        cv2.FONT_HERSHEY_SIMPLEX,
                        1.0, (255, 255, 255))


    sendx=str(math.floor(tx*(-45/573)+110))
    sendy=str(math.floor(ty*(-45/470)+110))
    
    if len(sendx)==2:
        sendx= '0'+ sendx
        
    elif len(sendx)==1:
        sendx='00'+ sendx
        
    elif len(sendx)<1 or len(sendx)>3:
        sendx='000'
        
    else:
        sendx=sendx

    # ensures that sendX is 3 bytes
    if len(sendy)==2:
        sendy='0'+sendy
    elif len(sendy)==1:
        sendy='00'+sendy
    elif len(sendy)<1 or len(sendy)>3:
        sendy='000'
    else:
        sendy=sendy

    #pirch and yaw positions ready to be sent
    send= sendy + sendx + shoot
   # print(sendp)
    ser.write(send.encode('utf-8'))
    time.sleep(.001)
    print(send)
    shoot = '0'
    
    # Program Termination
    cv2.imshow("Multiple Color Detection in Real-TIme", imageFrame)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        #cap.release()
        cv2.destroyAllWindows()
        break
