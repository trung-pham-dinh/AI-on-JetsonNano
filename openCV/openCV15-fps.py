import cv2
import time
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
currTime = preTime = 0
font = cv2.FONT_HERSHEY_DUPLEX
while True:
    _, frame = cam.read()

    currTime = time.time()
    fps = str( int(1/(currTime-preTime)))
    preTime = currTime
    cv2.putText(frame, fps, (10,50) ,font, 3, (255,255,0))

    cv2.imshow('piCam', frame)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           