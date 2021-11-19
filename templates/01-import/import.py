import sys
import requests

DATA_FILENAME = "covid-19.csv"

def getDataset(dataSource):
    # get dataset
    file = requests.get(dataSource)

    # save dataset
    with open(DATA_FILENAME, "wb") as f:        
        f.write(file.content)

if __name__ == "__main__":
    try:
        getDataset(sys.argv[1])
    except BaseException as exc:
        print("error download dataset.", exc)