# import cv2
# import glob
# import re

# img_array = []
# numbers = re.compile(r'(\d+)')
# def numericalSort(value):
#     parts = numbers.split(value)
#     parts[1::2] = map(int, parts[1::2])
#     return parts

# for filename in sorted(glob.glob('/Users/wilson006/Desktop/Vscode/New Ellicott Frames/*png')):
#     key = numericalSort
#     img = cv2.imread('/Users/wilson006/Desktop/Vscode/Cropped Video')
#     height, width, layers = img.shape
#     size = (width, height)
#     img_array.append(img)

# out = cv2.VideoWriter('/Users/wilson006/Desktop/Vscode/New Ellicott Frames/frame_0.png')

# for i in range(len(img_array)):
#     out.write(img_array[i])
#     out.release()

# import glob

# image = '/Users/wilson006/Desktop/Vscode/New Ellicott Frames/frame_1.png'
# #some stuff should go here 

# def order(x):
#     y = x[58: -4]
#     return int(y)

# # print(order(image))
# images = glob.glob('/Users/wilson006/Desktop/Vscode/New Ellicott Frames/*')

# for image in sorted(images, key = order):
#     print(image)


