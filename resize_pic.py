import cv2 as cv
from PIL import Image
import numpy as np
filename = r"C:\Users\75400\PycharmProjects\collect_data\Demo_pic\09.png"
img = cv.imread(filename)
resize_image = cv.resize(img, (100, 100))
img_resize = cv.cvtColor(resize_image, cv.COLOR_BGR2RGB)
im = Image.fromarray(img_resize)
im.save("9.png")