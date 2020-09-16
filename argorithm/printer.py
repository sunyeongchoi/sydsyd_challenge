def solution(priorities, location):
    answer = 0
    value = priorities[location]
    for i in range(len(priorities)):
        if value <= priorities.pop(0):
            answer += 1
    return answer


if __name__ == '__main__':
    real_answer = solution([1, 1, 9, 1, 1, 1],0)
    print(real_answer)
