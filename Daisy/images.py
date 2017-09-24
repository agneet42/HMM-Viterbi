import numpy as numpy
import cv2

img = cv2.imread('test.bmp',0)
res = cv2.resize(img,(48,48))
cv2.imwrite('resized.png',res)

from PIL import Image

file_in = "resized.png"
img = Image.open(file_in)
img.save('resized.bmp')


iname = 'comp0002.bmp'
oname = 'test.bmp'

img = Image.open(iname)
newimg = img.convert(mode='P',colors=8)
newimg.save('test.bmp')
