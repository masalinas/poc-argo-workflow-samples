import sys
import json
import pymongo

DATABASE = "argo"
COLLECTION = "covid"

def insertDataset(jsonDataset):
    # connect to database
    dbClient = pymongo.MongoClient("mongodb://192.168.1.57:27017/")
    db = dbClient[DATABASE]
    collection = db[COLLECTION]

    # recover dataset
    with open(jsonDataset, 'r') as jsonFile:
        data = json.load(jsonFile)        

        # insert dataset into database
        collection.insert_many(data)

if __name__ == "__main__":
    try:
        insertDataset(sys.argv[1])
    except BaseException as exc:
        print("error insert dataset.", exc)