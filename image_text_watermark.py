from PIL import Image
from PIL import ImageFont
from PIL import ImageDraw
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("input\\maison.png")
image.show()
plt.imshow(image)

# Target image
watermark_image = image.copy()

# image watermark
size = (500, 100)
nono_image = Image.open("input\\nono.jpg")
nono_image.thumbnail(size)

size = (500, 100)
clara_image = Image.open("input\\clara.jpg")
clara_image.thumbnail(size)

size = (500, 100)
romain_image = Image.open("input\\romain.jpg")
romain_image.thumbnail(size)

# Text watermark
draw = ImageDraw.Draw(watermark_image)
# ("font type",font size)
w, h = image.size
x, y = int(w / 2), int(h / 2)
if x > y:
  font_size = y
elif y > x:
  font_size = x
else:
  font_size = x
   
font = ImageFont.truetype("arial.ttf", int(font_size/6))
 
# add Watermark
# (0,0,0)-black color text
draw.text((x, 100), "La maison des ours", fill=(0, 0, 0), font=font, anchor='ms')
plt.subplot(1, 2, 1)
plt.title("black text")

 
# add watermark
watermark_image.paste(nono_image, (485, 280))
watermark_image.paste(clara_image, (300, 500))
watermark_image.paste(romain_image, (650, 500))
watermark_image.show()
plt.imshow(watermark_image)