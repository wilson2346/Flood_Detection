# import cv2

# source =  cv2.VideoCapture('/Users/wilson006/Desktop/Engineering 101/Test 1.mov')
# while True:
#      ret, img = source.read()
#      gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#      cv2.imshow("Live", gray)
#      key = cv2.waitKey(20) # seconds to let video play until the end 
#      if key == ord("q"):
#         break 


import cv2
capture = cv2.VideoCapture('/Users/wilson006/Desktop/Engineering 101/Test 1.mov')
success,image = capture.read()
count = 0
while success:
    cv2.imwrite("./frames/frame%d.jpg" % count, image) #save into computer file name
    success,image = capture.read()
    print('Read a new frame: ', success)
    count += 1