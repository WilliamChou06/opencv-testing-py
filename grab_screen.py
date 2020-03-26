import numpy as np
from PIL import ImageGrab
import cv2
import time

def process_img(original_image):
  grayscale_image = cv2.cvtColor(original_image, cv2.COLOR_BGR2GRAY)
  processed_image = cv2.Canny(grayscale_image, threshold1=50, threshold2=100)

  return processed_image


last_time = time.time() 
while(True):
    printscreen_pil =  ImageGrab.grab()
    screen =   np.array(printscreen_pil)
    new_screen = process_img(screen)
    
    print('Loop took {} seconds'.format(time.time() - last_time))
    last_time = time.time()

    # cv2.imshow('window', cv2.cvtColor(screen, cv2.COLOR_BGR2RGB))
    cv2.imshow('window', new_screen)

    if cv2.waitKey(25) & 0xFF == ord('q'):
        cv2.destroyAllWindows()
        break
        