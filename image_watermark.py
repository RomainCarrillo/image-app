from PIL import Image
import matplotlib.pyplot as plt
import numpy as np

image = Image.open("input\\maison.png")
image.show()
plt.imshow(image)

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
 
# add watermark
watermark_image = image.copy()
watermark_image.paste(nono_image, (485, 280))
watermark_image.paste(clara_image, (300, 500))
watermark_image.paste(romain_image, (650, 500))
watermark_image.show()
plt.imshow(watermark_image)