def solution(A):
    answer = []
    A.sort()
    for i in range(len(A)-1):
        answer.append(abs(A[i]-A[i+1]))
    return max(answer)//2

if __name__ == '__main__':
    real_answer = solution([5, 5])
    print(real_answer)