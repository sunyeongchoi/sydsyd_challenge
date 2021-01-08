import numpy as np


def solution(arr):
    n = 1
    return arr[:n, :n]


if __name__ == '__main__':
    real_answer = solution([[1, 1, 0, 0], [1, 0, 0, 0], [1, 0, 0, 1], [1, 1, 1, 1]])
    print('정답 : ', real_answer)
