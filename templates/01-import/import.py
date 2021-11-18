import requests

DATA_URL = "https://raw.githubusercontent.com/ec-jrc/COVID-19/master/data-by-country/jrc-covid-19-countries-latest.csv"
DATA_FILENAME = "covid-19.csv"

def getDataset():
    # get dataset
    file = requests.get(DATA_URL)    

    # save dataset
    with open(DATA_FILENAME, "wb") as f:        
        f.write(file.content)

if __name__ == "__main__":
    try:
        getDataset()
    except BaseException as exc:
        print("error download dataset.", exc)