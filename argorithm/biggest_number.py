def solution(numbers):
    answer = sorted(list(map(str, numbers)), key=lambda x: x*5, reverse=True)
    return str(int(''.join(answer)))


if __name__ == '__main__':
    real_answer = solution([6, 10, 2])
    print(real_answer)

