
import uix
from uix.elements import container, image, button
from uix_components import fabric
from PIL import Image, ImageDraw
import io
img = Image.new("RGB",(300,300),"white")

radius = 1

def drawCircle(draw,x,y,r,color):
    draw.ellipse((x-r,y-r,x+r,y+r),fill=color)


def drawImage(img):
    draw = ImageDraw.Draw(img)
    draw.rectangle((0,0,300,300),fill="white")
    drawCircle(draw,150,150,radius,"red")
    

def _root():
    with container(id="container1") as main:
        image(id = "image1", value = img).size(None,100).on("click",update)
        fabric(id="fabric1",width=300,height=300).bg("white")
    return main

def update(ctx,id,value):
    global radius
    radius += 5
    if radius > 150:
        radius = 1
    drawImage(img)
    ctx.session.elements["image1"].value = img

uix.start(ui = _root(), config = {"debug":True})