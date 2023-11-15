# Задание No1
# 📌 Возьмите любые 1 - 3 задачи из прошлых домашних заданий.
# Добавьте к ним логирование ошибок и полезной информации.
# Также реализуйте возможность запуска из командной строки с передачей параметров.

from ex_01_Matrix import Matrix
from ex_01_MyException import TwoWayEqualSizeException, OneWayEqualSizeException

mtrx_1 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrx_2 = Matrix([[5, -1, 6], [-3, 0, 7]])
mtrx_3 = Matrix([[2, 1], [-3, 0], [4, -1]])
mtrxs = (mtrx_1, mtrx_2, mtrx_3)
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
    main(mtrx_1, mtrx_3)
    main(mtrx_1, mtrx_2)