import cv2
print(cv2.__version__)
dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down

def nothing():
    pass

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)

# we will create a tracbar in a window
cv2.namedWindow('piCam') # forward declare
cv2.createTrackbar('xValue', 'piCam', 50, dispW, nothing)
#                  50 is the initial value of track bar which go from 0->500
cv2.createTrackbar('yValue', 'piCam', 50, dispH, nothing)
cv2.createTrackbar('boxWidth', 'piCam', 50, dispW, nothing)
cv2.createTrackbar('boxHeight', 'piCam', 50, dispH, nothing)
while True:
    _, frame = cam.read()
    xVal = cv2.getTrackbarPos('xValue', 'piCam')
    yVal = cv2.getTrackbarPos('yValue', 'piCam')
    bW = cv2.getTrackbarPos('boxWidth', 'piCam')
    bH = cv2.getTrackbarPos('boxHeight', 'piCam')

    cv2.circle(frame, (xVal, yVal), 5, (0,0,255), -1)
    cv2.rectangle(frame, (xVal, yVal), (xVal+bW, yVal+bH), (255,0,255), 4)
    

    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()  