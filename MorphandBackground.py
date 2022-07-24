from shutil import get_archive_formats
import cv2
from cv2 import cvtColor
from cv2 import erode
import numpy as np
import glob

image1 = cv2.imread('/Users/wilson006/Desktop/Vscode/Cleaner_Image/1.jpg')
image2 = cv2.imread('/Users/wilson006/Desktop/Vscode/Cleaner_Image/9906.jpg')

#Background Subtraction
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
graytwo = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
sub = cv2.subtract(graytwo, gray)

#Morphological Operations
ret, th = cv2.threshold(sub, 80, 255, cv2.THRESH_BINARY)
kernel = np.ones((2,2), np.uint8)
dilation = cv2.dilate(th, kernel, iterations = 1)


cv2.imshow('image1', gray)
cv2.imshow('image2', graytwo)
cv2.imshow('outsub', sub)
# cv2.imshow('threshold', th)
# cv2.imshow('dilate', dilation)

cv2.waitKey(0)
