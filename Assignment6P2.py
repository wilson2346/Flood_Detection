import cv2 as cv

capture = cv.VideoCapture('/Users/wilson006/Desktop/Engineering 101/Test 1.mov')
while True:
    isTrue, frame = capture.read()
    cv.imshow('Video', frame)

    if cv.waitKey(30) & 0xFF==ord('q'): # "d" key to break out playing video 
        break

capture.release()
cv.destroyAllWindows()

