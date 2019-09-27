import cv2 as cv
import helpers.parser as parser
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import collections
import random

url = 'https://sun9-48.userapi.com/c847020/v847020566/c8d21/W818Vi80Yc0.jpg'

faceCascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')


cap = cv.VideoCapture(url)
ret,img = cap.read()

gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)

faces = faceCascade.detectMultiScale(gray,1.2,5,minSize=(20,20))
Coords = collections.namedtuple('Coord',['x','y'])

articles = parser.get()
xcoord = []
ycoord = []
for(x,y,w,h) in faces:
    cv.rectangle(img,(x,y),(x+w,y+h),(10,252,10),2)
    roi_gray = gray[y:y+h, x:x+w]
    roi_color = img[y:y+h, x:x+w]
    xcoord.append(x)
    ycoord.append(y)

img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
pil_im = Image.fromarray(img)

font = ImageFont.truetype('etelka.otf',15,encoding="unic")
draw = ImageDraw.Draw(pil_im)
width,height = pil_im.size
draw.rectangle(((0,height-(17*len(xcoord))),(width,height)),fill='black')

for i in range(len(xcoord)):
    text = articles[random.randrange(0,len(articles),1)]
    title = text[:text.rfind('.')]
    draw.text((xcoord[i],ycoord[i]-20),title,(10,252,10),font=font)
    draw.text((10,height-((i+1)*17)),text,(10,252,10),font=font)


pil_im.save('lel.jpg',format='JPEG')