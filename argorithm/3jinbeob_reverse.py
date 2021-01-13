def solution(n):
    answer = 0
    temp = []
    while n != 0:
        temp.append(n % 3)
        n = n // 3
    for index, t in enumerate(temp):
        answer += t * 3**(len(temp)-(index+1))
    return answer


if __name__ == '__main__':
    real_answer = solution(125)
    print(real_answer)
