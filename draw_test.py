import cv2

img = cv2.imread('whiskey.jpg')
imR = cv2.resize(img, (1366, 768))

cv2.line(imR,(0,0),(150,150),(255,255,255),15)
cv2.rectangle(imR,(15,25),(200,150),(0,0,255),15)

cv2.imshow('whiskey.jpg', imR)
cv2.waitKey(0)