import cv2
import numpy as np
from matplotlib import pyplot as plt

# greyscale also = 0
img = cv2.imread('whiskey.jpg', 0)

plt.imshow(img, cmap = 'gray', interpolation = 'bicubic')
plt.xticks([]), plt.yticks([])  # to hide tick values on X and Y axis
plt.plot([200,300,400],[100,200,300],'c', linewidth=5)
plt.show()
cv2.imwrite('whiskey_grayscale.png', img)