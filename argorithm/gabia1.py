import math
def solution(n):
    answer = 0
    p = 1
    while n >= 5**p:
        answer += math.floor(n/5**p)
        p += 1
    return answer

if __name__ == '__main__':
    print(solution(10))