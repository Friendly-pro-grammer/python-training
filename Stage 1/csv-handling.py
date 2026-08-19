import csv 
with open("Stage 1/data.csv","r") as file:
    reader =csv.reader(file)
    
    for row in reader:
        print(row)
#returns something like an array ['Amit', '20', 'Ahmedabad']

with open("Stage 1/data.csv","r") as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)

#writing to a csv file
with open("Stage 1/data.csv","w",newline="") as file:
    writer = csv.writer(file)
    writer.writerow(["Name","age","city"])
    rows = [
    ["Amit", 20, "Ahmedabad"],
    ["Rahul", 21, "Delhi"],
    ["John", 22, "Mumbai"]
]
    writer.writerows(rows)
    