import cv2 as cv
import PIL
from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw 
import collections
import random
import io

from articles import get

def set_omon_free(url):
    faceCascade = cv.CascadeClassifier('Cascades/haarcascade_frontalface_default.xml')
    cap = cv.VideoCapture(url)
    ret,img = cap.read()
    gray = cv.cvtColor(img,cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(img,1.2,5,minSize=(20,20))
    Coords = collections.namedtuple('Coord',['x','y'])

    articles = get()
    xcoord = []
    ycoord = []
    for(x,y,w,h) in faces:
        cv.rectangle(img,(x,y),(x+w,y+h),(10,252,10),2)
        xcoord.append(x)
        ycoord.append(y)

    img = cv.cvtColor(img, cv.COLOR_BGR2RGB)
    pil_im = Image.fromarray(img)

    width,height = pil_im.size
    fontsize1 = int(height/50)
    fontsize2 = int(width/75)

    font1 = ImageFont.truetype('etelka.otf',fontsize1,encoding="unic")
    font2 = ImageFont.truetype('etelka.otf',fontsize2,encoding="unic")
    draw = ImageDraw.Draw(pil_im)

    draw.rectangle(((0,height-((fontsize2+5)*len(xcoord))),(width,height)),fill='black')
    for i in range(len(xcoord)):
        text = articles[random.randrange(0,len(articles),1)]
        title = text[:text.rfind('.')]
        draw.text((xcoord[i],ycoord[i]-fontsize1-10),title,(10,252,10),font=font1)
        draw.text((10,height-((i+1)*(fontsize2+5))),text,(10,252,10),font=font2)


    byteIO = io.BytesIO()
    pil_im.save(byteIO,format='JPEG')
    byteIO.seek(0)
    return byteIO
