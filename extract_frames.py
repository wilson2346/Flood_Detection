import cv2
import numpy as np


img = cv2.imread("/Users/wilson006/Desktop/Vscode/Final Frames/frame_19835.png")
cv2.imshow('Image',img)
  
# counting the number of pixels
number_of_white_pix = np.sum(img)
number_of_black_pix = np.sum(img == 0)
  
print('Number of white pixels:', number_of_white_pix)
print('Number of black pixels:', number_of_black_pix)
   