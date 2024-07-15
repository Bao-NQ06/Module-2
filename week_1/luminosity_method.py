import matplotlib.image as mpimg
import numpy as np
img = mpimg.imread('dog.jpeg')
gray_img_03 = np.dot(img,[0.21,0.72,0.07])
print(gray_img_03[0,0])