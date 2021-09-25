from PIL import Image
import PIL
import os
import glob



file_name = 'myimage.jpg' ##Where you store the compressed image
picture = Image.open(file_name)
dim = picture.size
## Get dimensions of original image
print(f"This is the current width and height of the image: {dim}")

#You will then need to select the specific quality of image from 0 – 100:
picture.save("Compressed_"+file_name,optimize=True,quality=30)
compressed_picture = Image.open("Compressed_"+file_name)
compressed_dim = compressed_picture.size

## Get dimensions of compressed image
print(f"This is the current width and height of the  compressed image: {compressed_dim}")
