import csv
import sys
with open(sys.argv[1], 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    a = []
    maxid = 0
    for row in reader:
        row0 = int(row[0])
        row1 = int(row[1])
        if row1 > maxid:
            maxid = row1
        if row0 > maxid:
            maxid = row0
        a += [[row0,row1]]
ans = []
for i in range(maxid+1):
    ans+=[[0,0,0,0,0]]
for node in a:
    ans[node[0]][0]+=1
    ans[node[1]][1]+=1
for node in a:
    ans[node[0]][2]+=ans[node[1]][0]
    ans[node[1]][3]+=ans[node[0]][1]
    ans[node[1]][4]+=ans[node[0]][0]-1
print(ans[1:])
        