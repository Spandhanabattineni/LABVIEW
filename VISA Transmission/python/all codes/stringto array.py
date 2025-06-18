import csv
with open("sample sheet.csv", 'r') as f:
     a = csv.reader(f)
     for row in a:
         print(row[0])

