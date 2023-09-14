import csv

graph = [
    [1,-1],
    [2,1],
    [3,2],
    [4,2],
    [5,4],
    [6,4],
    [7,5],
    [8,5],
]

with open('graph.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['nodeid', 'parentid'])
    writer.writeheader()
    for node in graph:
        parent = node[1]
        writer.writerow({'nodeid': node[0], 'parentid': parent})