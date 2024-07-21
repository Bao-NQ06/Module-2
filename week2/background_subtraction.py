import cv2
import numpy as np

img_size = (678,318)

bg_1 = cv2.imread('Module-2\week2\image\GreenBackground.png')
bg_1 = cv2.resize(bg_1,img_size)

bg_2 = cv2.imread('Module-2\\week2\\image\\NewBackground.jpg')
bg_2 = cv2.resize(bg_2,img_size)

object = cv2.imread('Module-2\week2\image\Object.png')
object = cv2.resize(object,img_size)



def compute_difference(bg_img, input_img):
    difference_three_channel = cv2.absdiff(bg_img, input_img)
    difference_single_channel = np.sum(difference_three_channel, axis=2) / 3.0
    difference_single_channel = difference_single_channel.astype('uint8')

    return difference_single_channel

def compute_binary_mask(difference_single_channel):
    difference_binary = np.where(difference_single_channel >= 15, 255, 0)
    difference_binary = np.stack((difference_binary,)*3, axis=-1)
    return difference_binary


def replace_background(bg1_image, bg2_image, ob_image):
    difference_single_channel = compute_difference(bg1_image,ob_image)
    binary_mask = compute_binary_mask(difference_single_channel)

    output = np.where(binary_mask==255, ob_image, bg2_image)

    return output

window_name = 'image'

cv2.imshow(window_name, replace_background(bg_1,bg_2,object)) 
  

cv2.waitKey(0) 

cv2.destroyAllWindows() 