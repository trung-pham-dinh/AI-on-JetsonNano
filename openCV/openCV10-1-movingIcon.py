import cv2
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2# try keep this ratio
flip = 2 # without it image will up-side down

pyLogo = cv2.imread('pl.jpg')
pyLogo = cv2.resize(pyLogo, (100, 100))[8:92,8:92] # size 84x84
pyLogoGray = cv2.cvtColor(pyLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('pyLogo', pyLogo);cv2.moveWindow('pyLogo', 705,0)

_,BGMask = cv2.threshold(pyLogoGray, 240, 255, cv2.THRESH_BINARY)
cv2.imshow('BGMask', BGMask); cv2.moveWindow('BGMask', 705, 150)

FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FGMask', FGMask); cv2.moveWindow('FGMask', 805, 0)

FG = cv2.bitwise_and(pyLogo, pyLogo, mask = FGMask)
cv2.imshow('FG', FG); cv2.moveWindow('FG', 805, 150)


camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)

x,y = 270,190
direction = [4,3]
edge = 84
while True:
    _, frame = cam.read()

    roi = frame[y:y+edge , x:x+edge]
    BG = cv2.bitwise_and(roi, roi, mask = BGMask)
   
    comp = cv2.add(BG,FG)
    frame[y:y+edge ,x:x+edge] = comp[:,:]

    x += direction[0]
    y += direction[1]

    if x <= 0 or x+edge >= dispW:
        direction[0] *= -1
        if x < 0 : x = 0
        elif x+edge > dispW: x = dispW-edge
    elif y <= 0 or y+edge >= dispH:
        direction[1] *= -1
        if y < 0 : y = 0
        elif y+edge > dispH: y = dispH-edge


    cv2.imshow('piCam', frame); cv2.moveWindow('piCam', 0, 0)
    cv2.imshow('BG', BG); cv2.moveWindow('BG', 705, 250)
    cv2.imshow('comp', comp); cv2.moveWindow('comp', 805, 250)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           