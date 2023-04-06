class Matrix:
    def __init__(self, v_matrix):
        self.v_matrix = v_matrix

    def __str__(self):
        new_matrix = []
        for row in self.v_matrix:
            new_matrix.append(' '.join([str(j) for j in row]))
        return '\n'.join(new_matrix)

    def __add__(self, other):
        new_matrix = []
        for i, row in enumerate(self.v_matrix):
            new_list = list(map(lambda x, y: x + y, row, other.v_matrix[i]))
            new_matrix.append(new_list)
        return Matrix(new_matrix)


my_martix1 = [[3, 5, 8, 3], [8, 3, 7, 1]]
my_martix2 = [[3, 5, 8, 3], [8, 3, 7, 1]]

obj_matrix1 = Matrix(my_martix1)
obj_matrix2 = Matrix(my_martix2)
obj_matrix3 = obj_matrix1 + obj_matrix2

print(obj_matrix1, end='\n\n')
print(obj_matrix2, end='\n\n')
print(obj_matrix3)
