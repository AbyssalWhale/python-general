import csv


with open("Tools/testFiles/testData.csv", "w") as file:
    # csv writer
    writer = csv.writer(file)
    writer.writerow(["transaction_Id", "product_Id", "price"])
    writer.writerow([100, 1, "100$"])
    writer.writerow([1000, 5, "1030$"])
    writer.writerow([1001, 3, "1200$"])
    writer.writerow([1002, 2, "1001$"])

with open("Tools/testFiles/testData.csv", "r") as file:
    # csv reader
    reader = csv.reader(file)
    # print(list(reader))
    for row in reader:
        print(row)
