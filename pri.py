import csv
a=open("data2.csv","r",encoding="utf-8")
data=csv.reader(a)
for i in data:
    print(i)
    input()