import glob

image = '/Users/wilson006/Desktop/Vscode/Ellicott Frames/frame1620.jpg'
# print(image[53:-4])

def order(x):
    y = x[53: -4]
    return int(y)

# print(order(image))
images = glob.glob('/Users/wilson006/Desktop/Vscode/Ellicott Frames/*')

for image in sorted(images, key = order):
    print(image)
