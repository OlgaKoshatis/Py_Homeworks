from random import randint


def print_matrix(matrix):
    """
    Вывод переданной матрицы в терминал!
    :param matrix:
    """
    for i in matrix:
        for j in i:
            print(j, end='\t')
        print()


class Matrix:
    """
    Класс для создания матрицы с рандомно заданными значениями
    """
    def __init__(self, height: int, width: int):
        """
        Параметры:
        :param height:
        :param width:
        Поля:
        matrix - Матрица в виде Списка списков
        summ_element_matrix - Сумма всех элементов матрицы
        """
        self.height = height
        self.width = width
        self.matrix = []
        self.summ_element_matrix = 0

    def to_create_matrix(self):
        """
        Создание рандомно заполненной матрицы
        И подсчёт суммы всех элементов данной матрицы
        с передачей результатов в поля класса
        self.matrix =
        self.summ_element_matrix =
        """
        for _ in range(self.height):
            row_matrix = []
            for _ in range(self.width):
                row_matrix.append(randint(1, 9))
            self.matrix.append(row_matrix)
        for i in self.matrix:
            for j in i:
                self.summ_element_matrix += j

    def summa_matrix(self, matrix):
        """
        Сумма данной матрицы с переданной ей в аргументы
        :param matrix: - Матрица
        :return: new_matrix - Результат сложения двух матриц
        """
        new_matrix = []
        row_matrix = []
        for count_1, count_2 in zip(self.matrix, matrix):
            for i, j in zip(count_1, count_2):
                row_matrix.append(i + j)
            new_matrix.append(row_matrix)
            row_matrix = []
        return new_matrix

    def print_matrix(self):
        """
        :return:
        """
        print('Matrix:')
        for i in self.matrix:
            for j in i:
                print(str(j), end='\t')
            print()

    def __str__(self):
        return f'Matrix: = {self.print_matrix()})'

    def __repr__(self):
        print(f'Matrix({self.height}, {self.width})')

    def __eq__(self, other):
        return self.summ_element_matrix == other.summ_element_matrix

    def __gt__(self, other):
        return self.summ_element_matrix > other.summ_element_matrix

    def __le__(self, other):
        return self.summ_element_matrix >= other.summ_element_matrix
    

    def multiplication_matrix(self, other):
        """
        Умножение матрицы на матрицу с проверкой размеров
        :param other: matrix - вторая матрица
        :return: new_matrix - результат умножения двух матриц
        """
        
        if not isinstance(other, self.__class__):
            raise TypeError("Not a 'Matrix'-type object")
        if self._cols != other._rows:
            raise ValueError("Operation not permitted if rows amount of first matrix "
                             "is not equal to columns amount of other one")
        new_matrix = [[0 for _ in range(other._rows)] for _ in range(self._rows)]
        for j in range(self._rows):
            for i in range(other._rows):
                new_matrix[j][i] = self._a_matrix[j][i] * other._a_matrix[i][j]
        return new_matrix
