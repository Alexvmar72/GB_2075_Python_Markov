from typing import List


class Matrix:
    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix
        for place in matrix:
            if len(place) != len(matrix[0]):
                raise ValueError('fail initialization matrix')


    def __str__(self):
        tmp_str = ''
        for size in self.matrix:
            tmp_str += '|'
            for plc in size:
                tmp_str +=' ' + str(plc)
            tmp_str += ' |\n'
        return tmp_str


    def __add__(self, other):
        if isinstance(other, Matrix):
            tmp_mtx = self.matrix.copy()
            for i, size in enumerate(self.matrix):
                for f, siz_2 in enumerate(size):
                    tmp_mtx[i][f] = siz_2 + other.matrix[i][f]
            return Matrix(tmp_mtx)


if __name__ == '__main__':
    first_matrix = Matrix([[1, 2], [3, 4], [5, 6]])
    second_matrix = Matrix([[6, 5], [4, 3], [2, 1]])
    print(first_matrix)
    print(first_matrix + second_matrix)
    fail_matrix = Matrix([[1, 2], [3, 4, 7], [5, 6]])