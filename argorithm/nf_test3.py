def solution(A):
    answer = []
    sumval=0
    for i in A:
        if i<0:
            answer.append(sumval)
            sumval=0
        else:
            sumval+=i
    answer.append(sumval)
    return max(answer)

if __name__ == '__main__':
    real_answer = solution([-8,3,0,5,-3,12])
    print(real_answer)