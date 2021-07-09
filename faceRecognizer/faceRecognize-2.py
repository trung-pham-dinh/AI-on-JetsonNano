import face_recognition
import cv2
print(cv2.__version__)

# face reading
donaldFace = face_recognition.load_image_file('/home/trungpham/Desktop/PythonProjects/faceRecognizer/demoImages/known/Donald Trump.jpg')
donaldEncode = face_recognition.face_encodings(donaldFace)[0] # encoding all face exist in image and we choose the first encode(the only face in image)

nancyFace = face_recognition.load_image_file('/home/trungpham/Desktop/PythonProjects/faceRecognizer/demoImages/known/Nancy Pelosi.jpg')
nancyEncode = face_recognition.face_encodings(nancyFace)[0]

trungFace = face_recognition.load_image_file('/home/trungpham/Desktop/PythonProjects/faceRecognizer/demoImages/known/myself.jpg')
trungEncode = face_recognition.face_encodings(trungFace)[0]

hanFace = face_recognition.load_image_file('/home/trungpham/Desktop/PythonProjects/faceRecognizer/demoImages/known/Voiu2.jpg')
hanEncode = face_recognition.face_encodings(hanFace)[0]

Encodings = [donaldEncode, nancyEncode,  hanEncode]
Names = ['Donald Trump', 'Nancy Pelosi', 'Vo iu']


# face matching 
font = cv2.FONT_HERSHEY_SIMPLEX
testImage = face_recognition.load_image_file('/home/trungpham/Desktop/PythonProjects/faceRecognizer/demoImages/unknown/u18.jpg')
faceLocations = face_recognition.face_locations(testImage)
allEncodings = face_recognition.face_encodings(testImage, faceLocations)

testImage = cv2.cvtColor(testImage, cv2.COLOR_RGB2BGR)

# (top right, bottom left)
for (row1,col1,row2,col2), face_encoding in zip (faceLocations, allEncodings):
    name = 'Unknown Person'
    matches = face_recognition.compare_faces(Encodings, face_encoding)
    if True in matches:
        first_match_index = matches.index(True)
        name = Names[first_match_index]
    cv2.rectangle(testImage, (col2,row1), (col1,row2), (0,255,0), 2)
    cv2.putText(testImage, name ,(col2,row1-10), font, 0.75, (255,0,0), 3)

cv2.imshow('myWindow', testImage)
cv2.moveWindow('myWindow', 0,0)
if cv2.waitKey(0) == ord('q'):
    cv2.destroyAllWindows()