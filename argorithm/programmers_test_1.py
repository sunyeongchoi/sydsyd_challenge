def solution(numbers):
    answer = []
    while len(numbers) != 1:
        first = numbers.pop(0)
        for number in numbers:
            answer.append(number+first)
    answer = list(set(answer))
    answer.sort()
    return answer


if __name__ == '__main__':
    real_answer = solution([5,0,2,7])
    print('출력값: ', real_answer)