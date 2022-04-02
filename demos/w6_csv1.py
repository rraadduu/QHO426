#Import csv file
import csv
#Open the csv file in read only mode and name it 'file' as temporary name
with open('studentcity.csv', 'r') as file:
  #To read csv files use csv.reader (list)
  reader = csv.reader(file)
  #dictionary form
  #reader = csv.DictReader(file)
  #open in different versions ussing delimiter like one string
  #reader = csv.reader(file, delimiter = '\t')
  for row in reader:#read the file row by row
    print(row)