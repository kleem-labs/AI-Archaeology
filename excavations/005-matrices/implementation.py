"""Build matrix-vector and matrix-matrix multiplication from scratch."""


def matrix_vector(matrix, vector):
    if not matrix or any(len(row) != len(vector) for row in matrix):
        raise ValueError("every matrix row must match the vector size")
    return [sum(weight * value for weight, value in zip(row, vector))
            for row in matrix]


def transpose(matrix):
    if not matrix or any(len(row) != len(matrix[0]) for row in matrix):
        raise ValueError("matrix must be non-empty and rectangular")
    return [list(column) for column in zip(*matrix)]


def matrix_matrix(left, right):
    right_columns = transpose(right)
    if any(len(row) != len(right) for row in left):
        raise ValueError("inner matrix dimensions must agree")
    return [[sum(a * b for a, b in zip(row, column))
             for column in right_columns] for row in left]


if __name__ == "__main__":
    point = [2, 1]
    scale = [[2, 0], [0, 3]]
    rotate_90 = [[0, -1], [1, 0]]
    composed = matrix_matrix(rotate_90, scale)
    print("point:", point)
    print("scaled:", matrix_vector(scale, point))
    print("scaled then rotated:", matrix_vector(composed, point))
    print("composed matrix:", composed)
