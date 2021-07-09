import cv2
print(cv2.__version__)
dispW = 320 # display width
dispH = 240 # try keep this ratio
flip = 2 # without it image will up-side down

cvLogo = cv2.imread('cv.jpg')
cvLogo = cv2.resize(cvLogo, (320, 240))
# we need convert to gray before masking
cvLogoGray = cv2.cvtColor(cvLogo, cv2.COLOR_BGR2GRAY)
cv2.imshow('cvLogoGray', cvLogoGray)
cv2.moveWindow('cvLogoGray', 0, 265)

_,BGMask = cv2.threshold(cvLogoGray, 180, 255, cv2.THRESH_BINARY)
# if the value of pixel is < threshold: value become 0 (black)
# if the value of pixel is >= threshold: value become 255(white) -> binarythresh
cv2.imshow('BG Mask', BGMask)
cv2.moveWindow('BG Mask', 385,0)


FGMask = cv2.bitwise_not(BGMask)
cv2.imshow('FG Mask', FGMask)
cv2.moveWindow('FG Mask', 385, 265)

FG = cv2.bitwise_and(cvLogo, cvLogo, mask = FGMask)
cv2.imshow('FG image', FG)
cv2.moveWindow('FG image', 705, 265)


cv2.namedWindow('Blended')
cv2.createTrackbar('BlendValue', 'Blended', 50, 100, lambda x:None)

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
while True:
    _, frame = cam.read()
    BG = cv2.bitwise_and(frame, frame, mask = BGMask)

    
    compImage = cv2.add(BG, FG)

    percent = cv2.getTrackbarPos('BlendValue', 'Blended') / 100

    blended = cv2.addWeighted(frame, 1-percent, cvLogo, percent, 0) # 50% of frame and 50% of cvlogo

    blendFG = cv2.bitwise_and(blended, blended, mask = FGMask)

    compBlendImage = cv2.add(blendFG, BG)


    cv2.imshow('piCam', frame)
    cv2.moveWindow('piCam', 0, 0)

    cv2.imshow('BGframe', BG)
    cv2.moveWindow('BGframe', 705, 0)

    cv2.imshow('composite image', compImage)
    cv2.moveWindow('composite image', 1025, 0)

    cv2.imshow('Blended', compBlendImage)
    cv2.moveWindow('Blended', 1025, 265)

    if cv2.waitKey(1)==ord('q'):
        break
cam.release()
cv2.destroyAllWindows()                                                                                                                                           