list_1 = [[31, 22], [37, 43]]
list_2 = [[1, 5, 8, 1], [3, 5, 8, 3], [3, 5, 8, 3], [3, 2, 6, 3]]
list_3 = [[51, 86], [9, 2]]


class Matrix:

    def __init__(self, main_list):
        self.main_list = main_list

    def __str__(self):
        list_print = ""
        for list_item in self.main_list:
            list_print += str(list_item) + "\n"
        return list_print[:-2]

    def __add__(self, other):
        new_matrix = list()
        for i in range(len(self.main_list)):
            new_matrix.append([])
            for j in range(len(self.main_list[i])):
                new_matrix[i].append(self.main_list[i][j] + other.main_list[i][j])
        list_print = ""
        for list_item in new_matrix:
            list_print += str(list_item) + "\n"
        return list_print


matrix_1, matrix_2, matrix_3 = Matrix(list_1), Matrix(list_2), Matrix(list_3)
print(matrix_1, "\n")
print(matrix_2, "\n")
print(matrix_3, "\n")
print(matrix_1 + matrix_3)
