import cv2
# print(cv2.__version__)
# # with this W and H the speed of camera is right
# dispW = 640 # display width
# dispH = 480 # try keep this ratio
# flip = 2 # without it image will up-side down
# camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
# #           g streamer          video format            native full resolution      
# cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
# outputVid = cv2.VideoWriter('videos/myCam.avi', cv2.VideoWriter_fourcc(*'XVID'), 21, (dispW, dispH)) # framerate = 21 equals framerate of object cam above

# while True:
#     _, frame = cam.read()
#     cv2.imshow('piCam', frame)
#     cv2.moveWindow('piCam', 0, 0)
#     outputVid.write(frame)
#     if cv2.waitKey(1)==ord('q'):
#         break
# cam.release()
# outputVid.release()
# cv2.destroyAllWindows() 



# read frame from what we save
# the video will be really fast
cam = cv2.VideoCapture('videos/myCam.avi')
while True:
    _, frame = cam.read()
    cv2.imshow('miCam.avi', frame)
    cv2.moveWindow('miCam.avi', 0, 0)
    if cv2.waitKey(48)==ord('q'): # fix to 1/21 s ~ 48ms will fix the fast issue
        break
cam.release()
outputVid.release()
cv2.destroyAllWindows()
