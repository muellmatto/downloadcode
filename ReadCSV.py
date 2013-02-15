import csv

f = open('codedatabase.csv', 'r')
reader = csv.reader(f)
oi=[]
for row in reader:
    oi.append( [ 0 , row ] )

f.close()

