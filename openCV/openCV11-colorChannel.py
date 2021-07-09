import cv2
import numpy as np
print(cv2.__version__)
dispW = 320 # display width
dispH = 240 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
blank = np.zeros([240,320,1], np.uint8)
while True:
    _, frame = cam.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # b = frame[:,:,0] # b = cv2.split(frame)[0]
    # g = frame[:,:,1] # g = cv2.split(frame)[1]
    # r = frame[:,:,2] # r = cv2.split(frame)[2]
    b,g,r = cv2.split(frame)

    # cv2.merge: args are 1 color channel matrices
    blue = cv2.merge((b,blank,blank)) # merge color channel
    green = cv2.merge((blank,g,blank))
    red = cv2.merge((blank,blank,r))

    b[:] = b[:]* 1.5
    merge = cv2.merge((b,g,r))

    cv2.imshow('piCam', frame);cv2.moveWindow('piCam', 0,0)
    cv2.imshow('blue', blue);cv2.moveWindow('blue', 385,0)
    cv2.imshow('green', green);cv2.moveWindow('green', 0,265)
    cv2.imshow('red', red);cv2.moveWindow('red', 385,265)
    cv2.imshow('merge', merge);cv2.moveWindow('merge', 705,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           