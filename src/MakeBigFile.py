import random
import csv

FILE_NAME = "./data/bigtestfile.data"
COLUMNS = 1000
ROWS = 1000000

if __name__ == "__main__":

    with open(FILE_NAME, "w") as file:
        write = csv.writer(file)
        for row in range(ROWS):
            data =  [ random.randint(0, 1000)  for numbers in range(COLUMNS) ]
            write.writerow(data)
