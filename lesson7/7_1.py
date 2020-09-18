# 1. Реализовать класс Matrix (матрица). Обеспечить перегрузку конструктора класса (метод __init__()),
# который должен принимать данные (список списков) для формирования матрицы.
# Подсказка: матрица — система некоторых математических величин, расположенных в виде прямоугольной схемы.
# Примеры матриц вы найдете в методичке.
# Следующий шаг — реализовать перегрузку метода __str__() для вывода матрицы в привычном виде.
# Далее реализовать перегрузку метода __add__() для реализации операции сложения двух объектов класса
# Matrix (двух матриц). Результатом сложения должна быть новая матрица.
# Подсказка: сложение элементов матриц выполнять поэлементно — первый элемент первой строки
# первой матрицы складываем с первым элементом первой строки второй матрицы и т.д.

numbers1 = [[21, 23, 2], [45, 21, 8], [9, 33, 24]]
numbers2 = [[15, 45, 1], [6, 12, 65], [19, 20, 13]]


class Matrix:
    def __init__(self, numbers):
        self.numbers = numbers

    def __str__(self):
        my_str = ''
        for el in self.numbers:
            for i in el:
                i = str(i)
                my_str += (i + ' ')
            my_str += '\n'
        return f'{my_str}'

    def __add__(self, other):
        if len(self.numbers) == len(other.numbers) and len(self.numbers[0]) == len(other.numbers[0]):
            for i in range(len(self.numbers)):
                for j in range(len(self.numbers[0])):
                    self.numbers[i][j] = self.numbers[i][j] + other.numbers[i][j]
            new_matrix = Matrix(self.numbers)
            return new_matrix
        else:
            print("Матрицы разных размеров нельзя складывать.")


matrix1 = Matrix(numbers1)
matrix2 = Matrix(numbers2)
print(matrix1)
print(matrix2)
print(matrix1 + matrix2)
