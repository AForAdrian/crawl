"""
Simple matrix multiplication module for PageRank calculations.
"""

def matmult(A, B):
    """
    Multiply two matrices A and B.

    Args:
        A (list of lists): First matrix
        B (list of lists): Second matrix

    Returns:
        list of lists: Result matrix
    """
    if not A or not B:
        return []

    rows_A = len(A)
    cols_A = len(A[0]) if A else 0
    rows_B = len(B)
    cols_B = len(B[0]) if B else 0

    if cols_A != rows_B:
        raise ValueError("Matrix dimensions don't match for multiplication")

    # Initialize result matrix
    result = [[0 for _ in range(cols_B)] for _ in range(rows_A)]

    # Perform multiplication
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                result[i][j] += A[i][k] * B[k][j]

    return result


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


def vecadd(a, b):
    """
    Add two vectors.

    Args:
        a (list): First vector
        b (list): Second vector

    Returns:
        list: Sum vector
    """
    if len(a) != len(b):
        raise ValueError("Vector lengths don't match")

    return [a[i] + b[i] for i in range(len(a))]


def vecmult(v, scalar):
    """
    Multiply vector by scalar.

    Args:
        v (list): Vector
        scalar (float): Scalar value

    Returns:
        list: Scaled vector
    """
    return [x * scalar for x in v]


def vecnorm(v):
    """
    Calculate Euclidean norm of vector.

    Args:
        v (list): Vector

    Returns:
        float: Euclidean norm
    """
    import math
    return math.sqrt(sum(x * x for x in v))
