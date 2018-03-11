import cv2

# Read in an image (roads) and convert to HSV
img = cv2.imread('img0301.jpg')
hsv = cv2.cvtColor(img, cv2.COLOR_BGR2HSV)
hsvlinedup = cv2.hconcat([hsv[:,:,0], hsv[:,:,1], hsv[:,:,2]])
cv2.imshow('test',hsvlinedup)
cv2.waitKey(0)

# Blur the image by convolution of a gaussian kernel
values = hsv[:,:,2];
blurred = cv2.GaussianBlur(values, (17,17), 5);
cv2.imshow('test',cv2.hconcat([values, blurred]))
cv2.waitKey(0)

# Canny
edges = cv2.Canny(blurred, 3, 45);
cv2.imshow('test',edges)
cv2.waitKey(0)

# Find Lines
lines = cv2.HoughLinesP(edges, 1, 3.14/180, 100);
print(lines.shape)
cv2.waitKey(0)

# Display image
disp = img
n = lines.shape[1]
for i in range(n):
    cv2.line(disp, (lines[0,i,0], lines[0,i,1]), (lines[0,i,2], lines[0,i,3]), (0,0,255))

cv2.imshow('test', disp)
cv2.waitKey(0)
