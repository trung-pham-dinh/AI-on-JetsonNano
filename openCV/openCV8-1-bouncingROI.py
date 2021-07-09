import cv2
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
direction = [4,4] # xvector, yvector
x,y = 320, 240
edge = 150
while True:
    _, frame = cam.read()
    
    cv2.rectangle(frame, (x, y), (x+edge, y+edge), (255,0,0), 4)

    smallFrame = frame[y:y+edge, x:x+edge].copy()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    frame = cv2.cvtColor(frame, cv2.COLOR_GRAY2BGR)
    frame[y:y+edge, x:x+edge] = smallFrame

    

    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0, 0)

    x += direction[0]
    y += direction[1]

    if x <= 0 or x+edge >= dispW:
        direction[0] *= -1
        if x < 0 : x = 0
        elif x > dispW: x = dispW
    elif y <= 0 or y+edge >= dispH:
        direction[1] *= -1
        if y < 0 : y = 0
        elif y > dispH: y = dispH
    


    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           