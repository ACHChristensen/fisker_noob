import cv2 as cv
from matplotlib import pyplot as plt
import math
import numpy as np

def resizing_image_squared(path_image,square_size):
    image = cv.imread(path_image)
    image_bgr = np.array(image)
    image = cv.cvtColor(image_bgr, cv.COLOR_BGR2RGB)
    #print(f"Shape size before resizing: {image.shape}")
    if (image.shape[0] >= image.shape[1]):
        resizing_factor = square_size/image.shape[0]
    else: 
        resizing_factor = square_size/image.shape[1]
    height_pixels = math.floor(image.shape[0]*resizing_factor)
    width_pixels= math.floor(image.shape[1]*resizing_factor)
    resized_img = cv.resize(image, (width_pixels,height_pixels))
    #print(f"After resizing: {resized_img.shape}")
    plt.imshow(resized_img)
    return resized_img


if __name__ == '__main__':
    print("This is the prepare_images module")