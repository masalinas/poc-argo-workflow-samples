import sys
import json

from csv import DictReader

DATA_PATH = "/mnt/dataset/"
DATA_FILENAME = "covid-19.csv"

def parser(csvDataset, jsonDataset):    
    # read csv dataset
    with open(DATA_PATH + csvDataset, 'r') as csvFile:                
        fieldnames = ("Date","iso3","CountryName","lat","lon","CumulativePositive","CumulativeDeceased","CumulativeRecovered","CurrentlyPositive","Hospitalized","IntensiveCare","EUcountry","EUCPMcountry","NUTS")
        csvReader = DictReader(csvFile, fieldnames)

        #convert csv dataset to json one
        with open(DATA_PATH + jsonDataset, 'w') as jsonFile: 
            jsonFile.write(json.dumps(list(csvReader)))
             
if __name__ == '__main__':
    try:
        # get csv dataset and set json dataset file name
        csvDataset = DATA_FILENAME
        jsonDataset = DATA_FILENAME.split('.')[0] + '.json'

        # json parser
        parser(csvDataset, jsonDataset)
    except BaseException as exc:
        print("error parsing sample data.", exc)