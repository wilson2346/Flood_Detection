# 1 Video to Frames 
import cv2
capture = cv2.VideoCapture('/Users/wilson006/Desktop/Vscode/Flood Video /Ellicott City 2018 Flood Multicam  REVISED.mp4')
success,image = capture.read()
count = 0
while success:
    cv2.imwrite("./Ellicott Frames/frame%d.jpg" % count, image) #save into computer file name
    success,image = capture.read()
    # print('Read a new frame: ', success)
    print(f"frame {str(count)} is done")
    count += 1
    if count == 25000:
        break
