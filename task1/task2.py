import csv
import sys
with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    a = []
    for row in reader:
        a += [[int(row[0]),int(row[1])]]
for node in a:
    sosedi = []
    if node[1] >= 0:
         sosedi+=[node[1]]
    for node2 in a:
        if node2[1] == node[0]:
             sosedi += [node2[0]]
    print("Node "+str(node[0])+":" + str(sosedi) + "\n")
        