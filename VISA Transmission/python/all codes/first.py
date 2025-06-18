
def read():
    act = open("sample sheet.csv")
    array = []
    rows = act.read().split('\n')  # or \r\n - it depends from your txt
    print(rows)
    act.close()

read()
