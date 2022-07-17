import cv2
import os
import glob

def order(x):
    y = x[51:-4]
    return int(y)

# def frames_to_video(output_path):
images = sorted(glob.glob('/Users/wilson006/Desktop/Vscode/Final Frames/*.png'), key = order)
frame_array =[]
size = None 
for i in range(len(images)):
    image = images[i]
    img = cv2.imread(image)
    height, width, layers = img.shape
    size = (width, height)

    frame_array.append(img)

fourcc = cv2.VideoWriter_fourcc(*'DIVX')
out = cv2.VideoWriter("/Users/wilson006/Desktop/Vscode/Final Video/cropped_video.mp4", fourcc, 30, size)

for i in range(len(frame_array)):
        out.write(frame_array[i])
out.release()