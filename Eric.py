print("Assignment 1")
print("Glob") #1
import glob
documents = glob.glob("/Users/wilson006/Desktop/Photo Dump/*.jpeg")
for image in documents:
   print(image)

print("Image") #2
import cv2

im = cv2.imread("/Users/wilson006/Desktop/Photo Dump/bridge.jpeg")
ima = cv2.imread("/Users/wilson006/Desktop/Photo Dump/waterfall.jpeg")

cv2.imshow("B", im)  #the name the picture when it comes up
cv2.imshow("W", ima)

cv2.waitKey(0) # ket to press to quit