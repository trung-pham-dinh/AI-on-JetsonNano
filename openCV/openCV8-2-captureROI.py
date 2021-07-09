import cv2
print(cv2.__version__)

rec = [[0,0],[0,0]] # [[x1,x2], [y1,y2]]
done = False
def captureROI(event, x, y, flag, params):
    global done # becase boolean is immutable so we need this
    if event == cv2.EVENT_LBUTTONDOWN:
        rec[0][0] = x; rec[1][0] = y # rec is mutable so do not need global
        done = False
    elif event == cv2.EVENT_LBUTTONUP:
        rec[0][1] = x; rec[1][1] = y
        done = True
    

dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)

cv2.namedWindow('piCam') # forward delare window for below function
cv2.setMouseCallback('piCam', captureROI)

while True:
    _, frame = cam.read()
    if done:
        x1,x2 =  sorted(rec[0])
        y1,y2 = sorted(rec[1])
        lineWidth = 4
        cv2.rectangle(frame, (x1,y1), (x2,y2), (255,0,0), lineWidth)
        roi = frame[y1+lineWidth//2:y2-lineWidth//2+1, x1+lineWidth//2:x2-lineWidth//2+1].copy() # we want to reference to a new separate object
        cv2.imshow('ROI', roi)
        cv2.moveWindow('ROI', 750, 0)

    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0, 0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()  
print(rec)                                                                                                                                         