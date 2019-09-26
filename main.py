import cv2 as cv

url = 'https://sun9-27.userapi.com/c850616/v850616113/18d820/cbvm7w50MqU.jpg'

faceCascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')


cap = cv.VideoCapture(url)
ret,img = cap.read()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,1.2,5,minSize=(20,20))

for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(255,0,0),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]

cv.imshow('img',img)
cv.waitKey() 