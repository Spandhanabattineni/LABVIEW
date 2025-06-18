
with open ("sample sheet.csv", 'r') as f:
    csvreader = csv.reader(f)
    for row in csvreader:
        print(row[0])
