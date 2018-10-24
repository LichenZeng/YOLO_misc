import numpy as np
from PIL import Image, ImageDraw

im = Image.open(r"D:\App_data\Deep_Learning_Data\yolo\VOCdevkit\VOC2012\JPEGImages\2007_000323.jpg")
w, h = im.size
print(w, " ", h)
draw = ImageDraw.Draw(im)
# draw.rectangle((277,3,500,375),outline='red')
# draw.rectangle((12,3,305,375),outline="red")
# im.show()
d_x1 = int(12 * (224 / w))
d_y1 = int(3 * (224 / h))
d_x2 = int(305 * (224 / w))
d_y2 = int(375 * (224 / h))
dImg = im.resize((224, 224), Image.ANTIALIAS)

d_draw = ImageDraw.Draw(dImg)
d_draw.rectangle((d_x1, d_y1, d_x2, d_y2), outline="red")
dImg.show()
