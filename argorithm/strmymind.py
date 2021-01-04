def solution(strings, n):
    answer = sorted(sorted(strings), key=lambda x:x[n])
    return answer


if __name__ == '__main__':
    real_answer = solution(['sun', 'bed', 'car'], 1)
    print('정답 : ', real_answer)
