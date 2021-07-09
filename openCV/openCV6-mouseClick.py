import cv2
import numpy as np
print(cv2.__version__)

evt = -1
pnts = []
img = np.zeros((255, 250, 3),               np.uint8) 
# rows, cols, number of values in a element(BGR values)
def click(event, x, y, flag, params):
	global pnt
	global evt
	if event == cv2.EVENT_LBUTTONDOWN:
		print('Mouse Event Was: ', event)
		print(x, ',', y)
		pnt = (x,y)
		pnts.append(pnt)
		evt = event
	if event == cv2.EVENT_RBUTTONDOWN:
		print('Mouse Event Was: ', event)
		blue = frame[y,x,0] # pick color blue of a pixel
		green = frame[y,x,1]
		red = frame[y,x,2]
		print(blue, green, red)

		colorString = str(blue) + ',' + str(green) + ',' + str(red)
		img[:]=[blue,green, red]
		fnt = cv2.FONT_HERSHEY_PLAIN
		r = 255-int(red) # we want to have a string color opposite with the color of what we grab
		g = 255-int(green)
		b = 255-int(blue)
		tp = (b,g,r)
		cv2.putText(img, colorString, (10,25), fnt, 1, tp, 2)
		cv2.imshow('myColor', img) # display a color window
        

dispW = 320*2 # display width
dispH = 240*2 # try keep this ratio
flip = 2 # without it image will up-side down

cv2.namedWindow('piCam') # forward delare window for below function
cv2.setMouseCallback('piCam', click)

camSet = 'nvarguscamerasrc !  video/x-raw(memory:NVMM), width=3264, height=2464, format=NV12, framerate=21/1 ! nvvidconv flip-method='+str(flip)+' ! video/x-raw, width='+str(dispW)+', height='+str(dispH)+', format=BGRx ! videoconvert ! video/x-raw, format=BGR ! appsink'
#           g streamer          video format            native full resolution      
cam = cv2.VideoCapture(camSet)  # CSI (rasberry pi camera)
#cam = cv2.VideoCapture(1)  # USB camera(webcam)
while True:
	_, frame = cam.read()
	# if evt == 1:
	# 	frame = cv2.circle(frame, pnt, 5, (255,0,0), -1)
	# 	font = cv2.FONT_HERSHEY_PLAIN
	# 	frame = cv2.putText(frame, str(pnt), pnt, font, 1, (255,0,0))
	for point in pnts:
		frame = cv2.circle(frame, point, 5, (255,0,0), -1)
		font = cv2.FONT_HERSHEY_PLAIN
		frame = cv2.putText(frame, str(point), point, font, 1, (255,0,0))
	cv2.imshow('piCam', frame)
	cv2.moveWindow('piCam', 0,0)

	keyStroke = cv2.waitKey(1)
	if keyStroke ==ord('c'):
		pnts.clear()
	if keyStroke ==ord('q'):
		break
cam.release()
cv2.destroyAllWindows()                                                                                                                           