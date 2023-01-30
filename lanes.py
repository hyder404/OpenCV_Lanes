import cv2
import numpy as np
import matplotlib.pyplot as plt

def canny(image): # Takes in an image and returns traced image through canny function
    gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
    blur = cv2.GaussianBlur(gray, (5, 5), 0)
    canny = cv2.Canny(blur, 50, 150)
    return canny

def region_of_interest(image): # Turns canny image into a general white masks and performs 'bitwise_and' to crop it
    height = image.shape[0]
    polygons = np.array([[(200,height),(1100,height),(550,250)]])
    mask = np.zeros_like(image)
    cv2.fillPoly(mask, polygons, 255)
    masked_image = cv2.bitwise_and(image,mask)
    return masked_image




image = cv2.imread('test_image.jpg') #reads image
lane_image = np.copy(image)
canny_traced = canny(image)
# plt.imshow(canny_traced)
# plt.show()
cropped_image = region_of_interest(canny_traced)
cv2.imshow("result", cropped_image) #shows image
cv2.waitKey(0) #sustains image on screen for indefinate time