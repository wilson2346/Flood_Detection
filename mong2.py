from pymongo import MongoClient
import datetime
import cv2
import glob
import numpy as np
import os
import time 


cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
print(client.list_database_names())
db = client.test 
print(db.list_collection_names())

def order(x):
    y = x[51:-4]
    return int(y)
frameNR = 0
for image_path in sorted(glob.glob("/Users/wilson006/Desktop/Vscode/Final Frames/*.png"), key=order):
    image = cv2.imread(image_path)
    #Pixels
    number_of_white_pix = np.sum(image)
    print('Number of white pixels:', number_of_white_pix)
    reu1 = {"frame number": frameNR, "number of pixel": int(number_of_white_pix)}
    reu = db.board
    reu.insert_one(reu1)
    frameNR= frameNR+1
    # time.sleep(1) 
   
  
    
 

