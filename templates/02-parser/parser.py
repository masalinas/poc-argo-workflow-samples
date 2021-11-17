import sys
import csv

def parser(sample_path):
    # read sample data    
    with open(sample_path, 'rb') as csvfile:
        spamreader = csv.reader(csvfile, delimiter=',')
    
    print(spamreader)

if __name__ == '__main__':
    try:
        parser(sys.argv[1])
    except BaseException as exc:
        print("error parsing sample data.", exc)
