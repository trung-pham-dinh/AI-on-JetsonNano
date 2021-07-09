import cv2
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
while True:
    _, frame = cam.read()
    frameGray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frameSmall = cv2.resize(frame, (320, 240))
    frameGraySmall = cv2.resize(frameGray, (320,240))

    cv2.imshow('small', frameSmall)
    cv2.moveWindow('small', 0,0)
    cv2.imshow('small gray', frameGraySmall)
    cv2.moveWindow('small gray', 0,265)
    cv2.imshow('cam', frame)
    cv2.moveWindow('cam', 345,0)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           