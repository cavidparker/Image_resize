import cv2
img = cv2.imread('images/test21.jpg', cv2.IMREAD_UNCHANGED)
print('original Dimention:',img.shape)

width = 192
height = 256
dim = (width, height)

resized = cv2.resize(img, dim, interpolation = cv2.INTER_AREA)
print('REsize Dimention :', resized.shape)

cv2.imwrite('results.jpg',resized)