import csv

def reading():
  with open("students.csv") as students:
    csv_reader = csv.reader(students)
    next(csv_reader)
    for row in csv_reader:
      print(row[0])

reading()