import cv2

# reading and getting only the blues
img = cv2.imread('img0201.jpg');
cv2.imshow('Original',img)
blues = img[:,:,0];
cv2.imshow('Test',blues)
cv2.waitKey(0)


# thresholding with THRESH_BINARY
# the threshold function actually returns two values but the first is ignored
_,binary = cv2.threshold(blues, 128, 255, cv2.THRESH_BINARY)
cv2.imshow('Test',binary)
cv2.waitKey(0)

# inRange
# inRange is simlar but works on ranges, as well as multiple channels
# the below is like running 6 calls to threshold
binary = cv2.inRange(img, (85,85,0), (170,170,255))
cv2.imshow('Test',binary)
cv2.waitKey(0)

# HSV
# sometimes it may be better to look at images in different colour spaces
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvlinedup = cv2.hconcat([hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]])
cv2.imshow('test',hsvlinedup)
cv2.waitKey(0)
