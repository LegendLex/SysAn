import numpy as np

def multiplyMatrix(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    matrix = []
    for row in range(rows):
        matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = matrix1[row][col] * matrix2[row][col]

    return np.array(matrix)


def matrixORfunc(matrix1, matrix2):
    rows = len(matrix1)
    cols = len(matrix1[0])
    matrix = []
    for row in range(rows):
        matrix.append([0] * cols)

    for row in range(rows):
        for col in range(cols):
            matrix[row][col] = max(matrix1[row][col], matrix2[row][col])

    return matrix


def expertToMatrix(str_json: str):
    matrix = []
    n = 0

    str_json = str(str_json[1:-1])
    str_split = str_json.split(",")
    clusters = []
    cluster_read = False
    for substr in str_split:
        current_cluster = cluster_read
        if '[' in substr:
            substr = substr[1:]
            cluster_read = True
        if ']' in substr:
            substr = substr[:-1]
            cluster_read = False
        if substr != "":
            if not current_cluster:
                clusters.append([int(substr)])
            else:
                clusters[-1].append(int(substr))
    
    for cluster in clusters:
        n += len(cluster)
    for i in range(n):
        matrix.append([1] * n)

    worse = []
    for cluster in clusters:
        for worse_elem in worse:
            for elem in cluster:
                matrix[elem - 1][worse_elem - 1] = 0
        for elem in cluster:
            worse.append(int(elem))

    return np.array(matrix)


def clusterCalc(matrix, est1, est2):
    clusters = {}

    rows = len(matrix)
    cols = len(matrix[0])
    exclude=[]
    for row in range(rows):
        if row+1 in exclude:
            continue
        clusters[row + 1] = [row + 1]
        for col in range(row+1, cols):
            if matrix[row][col] == 0:
                clusters[row + 1].append(col + 1)
                exclude.append(col+1)

    result = []
    for k in clusters:
        break_mark = False
        if not result:
            result.append(clusters[k])
            continue
        for i, elem in enumerate(result):
            if np.sum(est1[elem[0] - 1]) == np.sum(est1[k - 1]) and np.sum(est2[elem[0] - 1]) == np.sum(est2[k - 1]):
                for c in clusters[k]:
                    result[i].append(c)
                break_mark = True
                break

            if np.sum(est1[elem[0] - 1]) < np.sum(est1[k - 1]) or np.sum(est2[elem[0] - 1]) < np.sum(est2[k - 1]):
                result = result[:i] + [clusters[k]] + result[i:]
                break_mark = True
                break
        if not break_mark:
            result.append(clusters[k])

    final = []
    for r in result:
        if len(r) == 1:
            final.append(r[0])
        else:
            final.append(r)
    return str(final)


def task(string1: str, string2: str):
    matr1 = expertToMatrix(string1)
    matr2 = expertToMatrix(string2)

    matrAND = multiplyMatrix(matr1, matr2)
    matrAND_T = multiplyMatrix(np.transpose(matr1), np.transpose(matr2))

    matrOR = matrixORfunc(matrAND, matrAND_T)
    clusters = clusterCalc(matrOR, matr1, matr2)
    return clusters

if __name__ == "__main__":
    # string1 = '[1,[2,3],4,[5,6,7],8,9,10]'
    # string2 = '[[1,2],[3,4,5],6,7,9,[8,10]]'
    string1 = '[[1],[2,3,4],[5,6,7],8,9,10]'
    string2 = '[[1,2,3],[4,5],6,7,9,[8,10]]'
    stringA = '[1,[2,3],4,[5,6,7],8,9,10]'
    stringB = '[[1,2],[3,4,5,],6,7,9,[8,10]]'
    stringL = '[1,[2,3],4,[5,6,7],8,9,10]'
    stringR = '[[1,3],[2,4,5,],6,7,8,[9,10]]'
    
    results = task(stringL, stringR)
    print(results)
