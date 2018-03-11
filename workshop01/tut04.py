import cv2

img = cv2.imread('img0401.jpg')
binary = cv2.inRange(img, (39, 188, 231), (55, 206, 246))
cv2.imshow('test', binary)
cv2.waitKey(0)
