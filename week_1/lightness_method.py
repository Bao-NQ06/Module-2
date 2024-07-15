import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('dog.jpeg')
max_channel = np.max(img, axis=2)
min_channel = np.min(img, axis=2)
gray_img_01 = (max_channel + min_channel) / 2
print(gray_img_01[0,0])