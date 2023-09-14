import csv
import sys
with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    i = 0
    for row in reader:
        if i==int(sys.argv[2]):
            if len(row) >= int(sys.argv[3]) + 1:
                print(row[int(sys.argv[3])])
        i+=1