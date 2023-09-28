import csv

graph = [
    [2,1],
    [3,2],
    [4,2],
    [5,4],
    [6,4],
#    [7,5],
#    [8,5],
]

with open('graph.csv', 'w', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=['node1', 'node2'])
    writer.writeheader()
    for node in graph:
        parent = node[0]
        writer.writerow({'node1': node[1], 'node2': parent})