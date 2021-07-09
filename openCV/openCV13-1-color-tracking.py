import cv2
import numpy as np
print(cv2.__version__)

cv2.namedWindow('Trackbars')
cv2.moveWindow('Trackbars', 1320,0)

cv2.createTrackbar('hueLowest', 'Trackbars', 50, 179, lambda x: None)
cv2.createTrackbar('hueHighest', 'Trackbars', 100, 179, lambda x: None)
# we need another range of hue because the 'red' case: red consists of two range: [0->~20] and [~160->179]
cv2.createTrackbar('hueLowest2', 'Trackbars', 50, 179, lambda x: None)
cv2.createTrackbar('hueHighest2', 'Trackbars', 100, 179, lambda x: None)
cv2.createTrackbar('satLowest', 'Trackbars', 100, 255, lambda x: None)
cv2.createTrackbar('satHighest', 'Trackbars', 255, 255, lambda x: None)
cv2.createTrackbar('valLowest', 'Trackbars', 100, 255, lambda x: None)
cv2.createTrackbar('valHighest', 'Trackbars', 255, 255, lambda x: None)

dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
while True:
    _, frame = cam.read()
    #frame = cv2.imread('smarties.png')
    

    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    hueLow = cv2.getTrackbarPos('hueLowest', 'Trackbars')
    hueHigh = cv2.getTrackbarPos('hueHighest', 'Trackbars')
    hueLow2 = cv2.getTrackbarPos('hueLowest2', 'Trackbars')
    hueHigh2 = cv2.getTrackbarPos('hueHighest2', 'Trackbars')
    satLow = cv2.getTrackbarPos('satLowest', 'Trackbars')
    satHigh = cv2.getTrackbarPos('satHighest', 'Trackbars')
    valLow = cv2.getTrackbarPos('valLowest', 'Trackbars')
    valHigh = cv2.getTrackbarPos('valHighest', 'Trackbars')

    lowerBound = np.array([hueLow, satLow, valLow])
    higherBound = np.array([hueHigh, satHigh, valHigh])

    lowerBound2 = np.array([hueLow2, satLow, valLow])
    higherBound2 = np.array([hueHigh2, satHigh, valHigh])

    FGMask = cv2.inRange(hsv, lowerBound, higherBound) # core function to create mask with hsv
    FGMask2 = cv2.inRange(hsv, lowerBound2, higherBound2)
    FGMaskComp = cv2.add(FGMask, FGMask2)
    cv2.imshow('FGmaskComp', FGMaskComp); cv2.moveWindow('FGmaskComp', 0,410)
    
    # find contours on the mask
    # cv2 4.1.1 just has 2 returned value, so contours,_ instead of _,qcontours,_
    contours,_ = cv2.findContours(FGMaskComp, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
    #                                        most outside contour    
    contours = sorted(contours, key = lambda x: cv2.contourArea(x), reverse = True)

    if len(contours):
        if cv2.contourArea(contours[0]) >= 50: #(pixels)
            (x,y,w,h) = cv2.boundingRect(contours[0])
            cv2.line(frame, (x+w//2, 0), (x+w//2, dispH), (0,255,0), 3)
            cv2.line(frame, (0, y+h//2), (dispW, y+h//2), (0,255,0), 3)
    
    cv2.imshow('piCam', frame); cv2.moveWindow('piCam', 0, 0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           