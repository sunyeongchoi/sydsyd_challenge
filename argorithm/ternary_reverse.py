import math

def solution(n):
    answer = 0
    namoji = []
    while n!=0:
        namoji.append(n % 3)
        n = n//3

    for i in range(0,len(namoji)):
        answer = answer + namoji[len(namoji)-1-i]*int(math.pow(3,i))
    return answer


if __name__ == '__main__':
    real_answer = solution(125)
    print(real_answer)