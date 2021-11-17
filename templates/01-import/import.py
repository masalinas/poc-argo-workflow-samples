import requests

DATA_URL = "https://geoportalgasolineras.es/downloadReportPlanes"
DATA_PARM = {"extension": "CSV"}
DATA_FILENAME = "gas.csv"

def getResource():
    # get sample open data
    file = requests.get(DATA_URL, DATA_PARM)

    # save sample data
    with open(DATA_FILENAME, "wb") as f:        
        f.write(file.content)

if __name__ == "__main__":
    try:
        getResource()
    except BaseException as exc:
        print("error download sample data.", exc)