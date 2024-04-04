import csv

with open('data/ARoomWithAView/quotations.csv','r') as f:
    reader = csv.reader(f, quotechar='"')
    for l in reader:
        print(l[4])

