# open text file in read mode
text_file = open(r"C:\Users\battines\Documents\PycharmProjects\sample sheet.csv", "r")

# read whole file to a string
data = text_file.read()

# close file
text_file.close()

print(data)