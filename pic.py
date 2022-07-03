import cv2

im = cv2.imread("/Users/wilson006/Desktop/Pictures/PIC.jpeg")
ima = cv2.imread("/Users/wilson006/Desktop/Pictures/universal-studios-orlando-NOWHIRE1017.jpg")

cv2.imshow("Me", im)
cv2.imshow("Fun", ima)

cv2.waitKey(0)