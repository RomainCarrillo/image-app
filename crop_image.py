import numpy as np
from PIL import Image, ImageDraw

image = Image.open("input\\romain.jpg")

h, w = image.size

# creating luminous image
lum_img = Image.new('L',[h,w] ,0) 
draw = ImageDraw.Draw(lum_img)
draw.pieslice([(0,0),(h,w)],0,360,fill=255)
img_arr = np.array(image)
lum_img_arr = np.array(lum_img)
light_circle = Image.fromarray(lum_img_arr)
light_circle.show()

final_img_arr = np.dstack((img_arr, lum_img_arr))
cropped_image = Image.fromarray(final_img_arr)
cropped_image.show()