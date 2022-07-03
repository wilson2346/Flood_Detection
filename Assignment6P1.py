print("Open CV")
import cv2 as cv 

img = cv.imread('/Users/wilson006/Desktop/Photo Dump/rock water.jpeg')
cv.imshow("Water", img)

gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY) #turn selected image color to gray frame
cv.imshow('Gray', gray)

test_jpg = cv.imwrite('/Users/wilson006/Desktop/Photo Dump/test.jpg', gray) #saves gray form of photo to computer file 

cv.waitKey(0)


