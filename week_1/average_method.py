import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('dog.jpeg')
gray_img_02 = np.mean(img,axis=2)
print(gray_img_02[0,0])