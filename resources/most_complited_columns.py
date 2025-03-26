
def percentage(file):
    total_rows = len(file)
    list = []

    # In each column let's see how many elements are not "null"
    for coloana in file.columns:
        not_missing = file[coloana].notnull().sum()
        percentage = (not_missing / total_rows) * 100
        list.append((coloana, percentage))

    list.sort(key=lambda x: x[1], reverse=True)
    for col, percentage in list:
        print(col, f"({percentage:.2f}%)")