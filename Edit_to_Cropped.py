#Put All Frames Into New Folder while Cropped(region)
from operator import le
import cv2
import numpy as np
import glob 

frame_3 = cv2.imread('/Users/wilson006/Desktop/Vscode/Ellicott Frames/frame3.jpg')
r = cv2.selectROI("Area", frame_3) #read the path of one image 

def order(x):
    y = x[53: -4]
    return int(y)
frameNR = 0
for image_path in sorted(glob.glob('/Users/wilson006/Desktop/Vscode/Ellicott Frames/frame*.jpg'), key = order):
    image = cv2.imread(image_path)
    cropped_image = image[int(r[1]):int(r[1]+r[3]), 
                      int(r[0]):int(r[0]+r[2])]
    cv2.imwrite(f'/Users/wilson006/Desktop/Vscode/New Ellicott Frames/frame_{frameNR}.png', cropped_image)
    frameNR = frameNR+1
    print(f"frame {str(frameNR)} is done")





