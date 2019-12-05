import csv

with open("house/house.csv") as f:
    reader = csv.DictReader(f)
    # for row in reader:
    #     print(row["loyer"])
    loyers = [float(row["loyer"]) / float(row["surface"]) for row in reader]
    print(sum(loyers)/len(loyers))