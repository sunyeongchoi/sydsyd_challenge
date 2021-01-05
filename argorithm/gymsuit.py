def solution(n, lost, reserve):
    _reserve = set(reserve) - set(lost)
    _lost = set(lost) - set(reserve)
    for i in _reserve:
        if i-1 in _lost:
            _lost.remove(i-1)
        elif i+1 in _lost:
            _lost.remove(i+1)
    return n - len(_lost)


if __name__ == '__main__':
    real_answer = solution(5, [2, 4], [1, 3, 5])
    print('정답 : ', real_answer)
