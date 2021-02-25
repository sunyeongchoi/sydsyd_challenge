def solution(priorities, location):
    answer = 0
    while(len(priorities)!=0):
        if priorities[0] < max(priorities[1:]):
            priorities.append(priorities.pop(0))
        else:
            pass
    return answer


if __name__ == '__main__':
    real_answer = solution([1, 1, 9, 1, 1, 1],0)
    print(real_answer)
