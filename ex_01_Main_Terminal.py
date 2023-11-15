import argparse
import logging

from ex_01_Matrix import Matrix
from ex_01_MyException import TwoWayEqualSizeException, OneWayEqualSizeException

logging.basicConfig(filename='ex_05.log', filemode='w', encoding='utf-8', level=logging.INFO)
logger = logging.getLogger(__name__)


def parse():
    parser = argparse.ArgumentParser(description='Матрицы')
    parser.add_argument('-m_1', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])
    parser.add_argument('-m_2', type=list[list], default=[[1, 1, 1], [1, 1, 1], [1, 1, 1]])

    args = parser.parse_args()

    return Matrix(args.m_1), Matrix(args.m_2)


mtrx_1, mtrx_2 = parse()
# mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
# mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
# mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrxs = (mtrx_1, mtrx_2)
for elem in mtrxs:
    print(repr(elem))
print('---')


def main(first: Matrix, second: Matrix):
    if not Matrix._eq_len(first, second):
        raise TwoWayEqualSizeException(first, second)
    else:
        print(first == second)
        print(first + second)

    if first.clmns != second.rows:
        raise OneWayEqualSizeException(first, second)
    else:
        print(first * second)


if __name__ == '__main__':
    main(mtrx_1, mtrx_2)


"""
python ex_01_Main_terminal.py
python ex_01_Main_terminal.py -m_1 2, 1, -3, 0, 4, -1 -m2 5, -1, 6, -3, 0, 7
"""