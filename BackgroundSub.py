import cv2
import numpy as np

#Select Images to Subtract From Each Other 
image1 = cv2.imread('/Users/wilson006/Desktop/Vscode/Cleaner_Image/2.jpg')
image2 = cv2.imread('/Users/wilson006/Desktop/Vscode/Cleaner_Image/24999.jpg')

#Image1 minus Image2
gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
graytwo = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY) 
sub = cv2.subtract(graytwo, gray)

#Show Combined Images 
cv2.imshow('Image After Subtraction', sub)

#Escape Key 
cv2.waitKey(0)





