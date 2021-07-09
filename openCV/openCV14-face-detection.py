import cv2
import time 
print(cv2.__version__)

# in face detection, we should reduce the resolution for faster running
dispW = 320 # display width
dispH = 240 # try keep this ratio
flip = 2 # without it image will up-side down
camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
face_cascade = cv2.CascadeClassifier('/home/trungpham/Desktop/PythonProjects/cascade/face.xml')
eye_cascade = cv2.CascadeClassifier('/home/trungpham/Desktop/PythonProjects/cascade/eye.xml')
#for calculate fps
preTime = time.time()
font = cv2.FONT_HERSHEY_DUPLEX
print(cv2.getBuildInformation())
print('check CUDA:',cv2.cuda.getCudaEnabledDeviceCount())
while True:
    _, frame = cam.read()

    currTime = time.time()
    fps = str( int(1/(currTime-preTime)))
    preTime = currTime
    cv2.putText(frame, fps, (10,50) ,font, 3, (255,255,0))


    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    #eyes = eye_cascade.detectMultiScale(gray, 1.3, 5)
    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x,y), (x+w, y+h), (255,0,0), 3)
    
    cv2.imshow('piCam', frame)
    cv2.moveWindow('nanoCam', 0,0)
    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           