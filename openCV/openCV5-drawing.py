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
    frame = cv2.rectangle(frame, (140, 100), (180, 140), (255,0,255), 4)
    #                         upper corner  bottom corner     BGR   line width
    frame = cv2.circle(frame, (320, 250), 50, (0,0,255), 5)
    #                          center  radius    BGR   line width(-1 will fill color)
    
    font = cv2.FONT_HERSHEY_DUPLEX
    frame = cv2.putText(frame, 'This is a string', (300,300), font, 1, (255,255,0))
    #                                                     location line width
    
    frame = cv2.line(frame, (10, 10), (630, 470), (0,0,0), 4)
    #                         begin     end

    frame = cv2.arrowedLine(frame, (10, 470), (630, 10), (255,255,255), 3)

    
    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           