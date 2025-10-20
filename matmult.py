# must return a new 2D list containing the result
# when the given matrix is multiplied by the given
# scalar int or float

def mult_scalar(matrix, scalar):
    new_matrix = []
    for row in matrix:
        new_row = []
        for item in row:
            new_item = (item * scalar)
            new_row.append(new_item)
        new_matrix.append(new_row)

    return new_matrix

# must return a new matrix that is the result of *
# matrix a by the matrix b

def mult_matrix(a, b):
    rows_a = len(a)
    cols_a = len(a[0])
    rows_b = len(b)
    cols_b = len(b[0])
    if cols_a != rows_b :
        return None
    result = []
    for item_a in range(rows_a):
        row = []
        for item_b in range (cols_b):
            row.append(0)
        result.append(row)
    for i in range(rows_a):
        for j in range(cols_b):
            for k in range (cols_a):
                result[i][j] += a[i][k] * b[k][j]

    return result


# this function accept two single-row matrices and
#calculates the euclidean distance btwn these 2
#vectors

import math
def euclidean_dist(a,b):
    if len(a) == len(b) :
        total = 0
        distance = 0
        for i in range (len(a[0])):
            distance += (a[0][i] - b[0][i])  ** 2
    else:
        return None

    return math.sqrt(distance)


# Multiply matrix A by vector v (required by searchdata.py)
def matvecmult(A, v):
    """
    Multiply matrix A by vector v.

    Args:
        A (list of lists): Matrix
        v (list): Vector

    Returns:
        list: Result vector
    """
    if not A or not v:
        return []

    rows_A = len(A)
    cols_A = len(A[0]) if A else 0

    if cols_A != len(v):
        raise ValueError("Matrix and vector dimensions don't match")

    result = [0] * rows_A

    for i in range(rows_A):
        for j in range(cols_A):
            result[i] += A[i][j] * v[j]

    return result
