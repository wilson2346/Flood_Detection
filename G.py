print("Glob")
import glob 
documents = glob.glob("/Users/wilson006/Desktop/Engineering 101/*.pdf")
for image in documents:
   print(image)