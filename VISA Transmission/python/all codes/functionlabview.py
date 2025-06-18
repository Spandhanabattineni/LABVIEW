import csv
with open ("sample sheet.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row[0])


        def read():
            file = open(r"C:\Users\battines\Documents\PycharmProjects\sample sheet.csv")
            a = file.read()
            for row in file:
                print(row[0])
            return (a)


