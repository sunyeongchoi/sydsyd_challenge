def solution(numbers):
    answer = set()
    for index1, i in enumerate(numbers):
        for index2, j in enumerate(numbers):
            if index1 != index2:
                answer.add(i+j)
    return sorted(list(answer))


if __name__ == '__main__':
    real_answer = solution([2, 1, 3, 4, 1])
    print(real_answer)

