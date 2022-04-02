import csv
#Open the csv file in write mode and when enter data it creates a new line
with open('movie.csv', 'w', newline='') as file:
    #To write something use csv.writer
    writer = csv.writer(file)
    #Write by row using writer.writerow(["","",""])
    writer.writerow(["SN", "Movie", "Character"])
    writer.writerow([1, "Lord of the Rings", "Frodo Baggins"])
    writer.writerow([2, "Harry Potter", "Harry Potter"])