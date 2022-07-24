from pymongo import MongoClient, mongo_client
import datetime

# cluster = "mongodb://localhost:27017"
# client = MongoClient(cluster)

# print(client.list_database_names())

# db = client.test 

# print(db.list_collection_names())

# reu1 = {"Frame number": "", "Number of pixels": "", "status": "open",
#         "tags": ["python", "coding"], "date": datetime.datetime.utcnow()}

# reu = db.reu

# result = reu.insert_one(reu1)

# import os



# import os

# count = 0
# dir_path = f'/Users/wilson006/Desktop/Vscode/Final Frames'
# for path in os.scandir(dir_path):
#     if path.is_file():
#         count += 1
# print('file count:', count)


# import cv2

# cap = cv2.VideoCapture("/Users/wilson006/Desktop/Vscode/Final Video/cropped_video.mp4")
# length = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
# print( length )

cluster = "mongodb://localhost:27017"
client = MongoClient(cluster)
print(client.list_database_names())
db = client.test 
print(db.list_collection_names())

reu1 = {"frame number": 12, "number of pixels": 45}
reu =db.reu
reu.insert_one(reu1)
