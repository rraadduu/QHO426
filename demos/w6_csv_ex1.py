import csv
#Function for reading a csv file
def reading_csv():#define function
  with open("students.csv") as students:#open file and give temp name
    csv_reader = csv.reader(students)#read students as csv_reader
    next(csv_reader)
    total = 0
    count = 0
    for row in csv_reader:#read data row by row
      print(row)
      total += int(row[2])#accessing index 3 from csv
      count+=1
    print(f"The average mark of Exam 1 was {total/count}")
#Function for writing in a csv file
def writing_csv():#define function
  with open("students.csv", "a") as s:
    csv_writer = csv.writer(s)
    while True:#create while loop to write/add more data in the csv file
      name = input("Enter name: ")
      id = input("Enter ID: ")
      e1 = int(input("Enter Exam 1: "))
      e2 = int(input("Enter Exam 2: "))
      #create a list and add it in the csv file
      csv_writer.writerow([name, id, e1, e2])#one row
      if input("Shall we stop? (type Y or N): ").upper() == "Y":#y or n to break or keep adding
        break

reading_csv()#call reading function before writing
writing_csv()#call writing function
reading_csv()#call reading functiion after writing