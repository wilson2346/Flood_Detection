import glob
import numpy as np
import cv2
from matplotlib import image, pyplot as plt

# import all image files with the .jpg extension
def order(x):
    y = x[58: -4]
    return int(y)

images = sorted(glob.glob("/Users/wilson006/Desktop/Vscode/New Ellicott Frames/*.png"), key=order)

name = 1

for w in range(len(images)):
    if w == 0:
        pass
    else: 
        image_set = images[w:w+30]
        e_list = []
        for m in image_set:
            e_list.append(cv2.imread(m))

        avg_image = e_list[0]
        for w in range(len(image_set)):
            if w ==0:
                pass
            else:
                alpha = 1.0/(w+1)
                beta = 1.0 -alpha
                avg_image = cv2.addWeighted (e_list[w], alpha, avg_image, beta, 0.0)
        cv2.imwrite(f'/Users/wilson006/Desktop/Vscode/Cleaner_Image/{name}.jpg', avg_image)
        name = name+1

print("Yeah Boy")
