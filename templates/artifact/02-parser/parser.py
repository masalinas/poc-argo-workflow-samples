import sys
import json

from csv import DictReader

def parser(csvDataset, jsonDataset):    
    # read csv dataset
    with open(csvDataset, 'r') as csvFile:                
        fieldnames = ("Date","iso3","CountryName","lat","lon","CumulativePositive","CumulativeDeceased","CumulativeRecovered","CurrentlyPositive","Hospitalized","IntensiveCare","EUcountry","EUCPMcountry","NUTS")
        csvReader = DictReader(csvFile, fieldnames)

        #convert csv dataset to json one
        with open(jsonDataset, 'w') as jsonFile: 
            jsonFile.write(json.dumps(list(csvReader)))
             
if __name__ == '__main__':
    try:
        # get csv dataset and set json dataset file name
        csvDataset = sys.argv[1]
        jsonDataset = sys.argv[1].split('.')[0] + '.json'

        # json parser
        parser(csvDataset, jsonDataset)
    except BaseException as exc:
        print("error parsing sample data.", exc)