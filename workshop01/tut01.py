import cv2

# Reads a image and stores it into a matrx
# all images are just 3D matrices (in python everything is stored as a numpy array)
mat = cv2.imread('img0101.jpg')
# Creates a window called Test and displays the image
cv2.imshow('Test', mat)
# pauses the program until a key is pressed
cv2.waitKey(0);

# get the size
print(mat.shape)
cv2.waitKey(0);

# getting just the blue channel (images are stored in BGR format)
blues = mat[:,:,0];
cv2.imshow('Test',blues);
cv2.waitKey(0);
