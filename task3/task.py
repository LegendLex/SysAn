import pandas as pd
import sys
import numpy as np

def task(var)->float:
    matrix = np.array(var)
    n = matrix.shape[0]
    total_entropy = 0
    for row in matrix:
        prob = row / (n - 1)
        prob = prob[prob != 0]
        entropy = -np.sum(prob * np.log2(prob))
        total_entropy += entropy
    return total_entropy

matrix = pd.read_csv(sys.argv[1], header=None)
print(task(matrix))