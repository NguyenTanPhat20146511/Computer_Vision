import cv2
img = cv2.imread('lena512.jpg')
img = cv2.resize(img , (200,200))
print(img.shape)
