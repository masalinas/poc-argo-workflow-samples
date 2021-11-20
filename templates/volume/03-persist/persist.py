import sys
import json
import pymongo

DATABASE = "argo"
COLLECTION = "covid"

DATA_PATH = "/mnt/dataset/"
DATA_FILENAME = "covid-19.json"

def insertDataset(jsonDataset):
    # connect to database
    dbClient = pymongo.MongoClient("mongodb://192.168.1.57:27017/")
    db = dbClient[DATABASE]
    collection = db[COLLECTION]

    # recover dataset
    with open(DATA_PATH + jsonDataset, 'r') as jsonFile:
        data = json.load(jsonFile)        

        # insert dataset into database
        collection.insert_many(data)

if __name__ == "__main__":
    try:
        insertDataset(DATA_FILENAME)
    except BaseException as exc:
        print("error insert dataset.", exc)