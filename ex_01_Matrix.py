import argparse
import logging

logging.basicConfig(filename='ex_01.log', filemode='w', encoding='utf-8',
                    level=logging.INFO)
logger = logging.getLogger(__name__)


class Matrix:
    _matrix: list[list[int | float]] = None
    _rows: int = None
    _clmns: int = None

    def __init__(self, matrix: list[list[int | float]]) -> None:
        """
        :param matrix: [[int | float]]  -> матрица размерностью rows X clmns
        :param rows: int                -> a number of rows
        :param clmns: int               -> a number of columns
        """
        self._matrix = matrix
        self._rows = len(matrix)
        self._clmns = len(matrix[0])

    @property
    def rows(self):
        return self._rows

    @property
    def clmns(self):
        return self._clmns

    def __repr__(self):
        """Строка-представление объекта класса Matrix"""
        return f'Matrix({self._matrix})'

    def _eq_len(self, other):
        """Метод сравнивает размерности матриц в двух направлениях"""
        return self._rows == other._rows and \
               self._clmns == other._clmns

    def __eq__(self, other):
        """ Метод сравнивает матрицы ОДИНАКОВОЙ размерности:
         Матрицы равны, если равны их соответствующие элементы.
         """
        flag = True
        if self is other:
            logger.info(f'СРАВНЕНИЕ: {self._matrix} = {other._matrix}')
            return flag
        else:
            for i in range(self._rows):
                for j in range(self._clmns):
                    if self._matrix[i][j] != other._matrix[i][j]:
                        flag = False
                        logger.info(f'СРАВНЕНИЕ: {self._matrix} != {other._matrix}')
                        break
        return flag

    def __add__(self, other):
        """Метод считает сумму матриц ОДИНАКОВОЙ размерности"""
        new_mtrx = [[0 for j in range(self._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(self._clmns):
                new_mtrx[i][j] = self._matrix[i][j] + other._matrix[i][j]
        logger.info(f'СЛОЖЕНИЕ: {self._matrix} + {other._matrix} = {new_mtrx}')
        return Matrix(new_mtrx)

    def __mul__(self, other):
        """Метод считает умножение матриц"""
        new_mtrx = [[0 for j in range(other._clmns)] for i in range(self._rows)]
        for i in range(self._rows):
            for j in range(other._clmns):
                for k in range(self._clmns):
                    new_mtrx[i][j] += self._matrix[i][k] * other._matrix[k][j]
        logger.info(f'УМНОЖЕНИЕ: {self._matrix} * {other._matrix} = {new_mtrx}')
        return Matrix(new_mtrx)

    @staticmethod
    def parse():
        parser = argparse.ArgumentParser(description='Матрицы')
        parser.add_argument('-m_1', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        parser.add_argument('-m_2', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
        parser.add_argument('-action', type=str, default='=')

        args = parser.parse_args()

        return Matrix(args.m_1), Matrix(args.m_2), args.action


if __name__ == '__main__':
    mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
    mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
    # mtrx_1, mtrx_2, action = Matrix.parse()
    # print(f'{mtrx_1} {action} {mtrx_2}')