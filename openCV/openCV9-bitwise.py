import cv2
import numpy as np
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down

img1 = np.zeros((480,640,1), np.uint8) # grayscale image
img1[0:480,0:320] = [255]
img2 = np.zeros((480,640,1), np.uint8) # grayscale image
img2[190:290, 270:370] = [255]

bitAnd = cv2.bitwise_and(img1, img2) # two args because same size
bitOr = cv2.bitwise_or(img1, img2)
bitXor = cv2.bitwise_xor(img1, img2)


camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
while True:
    _, frame = cam.read()
    frame = cv2.bitwise_and(frame, frame, mask = bitXor) # three args: not same size(BGR and Gray)
    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0, 0)

    # cv2.imshow('BitWise', bitXor)
    # cv2.moveWindow('BitWise', 700,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           