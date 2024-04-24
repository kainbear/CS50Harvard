import csv

workers = []

with open("19.2workers.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        workers.append({"name": row["name"], "gorod": row["gorod"]})

for worker in sorted(workers, key=lambda worker: worker["name"]):
    print(f"{worker['name']} lives in {worker['gorod']}")