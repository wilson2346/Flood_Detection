import glob
import numpy as np
import cv2

frame_1 = cv2.imread('/Users/wilson006/Desktop/Vscode/Cleaner_Image/1.jpg')


def order(x):
    y = x[46:-4]
    return int(y)
frameNR = 0
for image_path in sorted(glob.glob('/Users/wilson006/Desktop/Vscode/Cleaner_Image/*.jpg'), key = order):
    image = cv2.imread(image_path)
    gray = cv2.cvtColor(frame_1, cv2.COLOR_BGR2GRAY)
    graytwo = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    sub = cv2.subtract(graytwo, gray)
    #Morph
    ret, th = cv2.threshold(sub, 80, 255, cv2.THRESH_BINARY)
    kernel = np.ones((2,2), np.uint8)
    dilation = cv2.dilate(th, kernel, iterations = 1)
    cv2.imwrite(f'/Users/wilson006/Desktop/Vscode/Final Frames/frame_{frameNR}.png', dilation)
    frameNR = frameNR+1
    print(f"frame {str(frameNR)} is done")


