def solution(A):
    answer = []
    SA = set(A)
    for i in SA:
        cnt = 0
        for j in A:
            cnt += abs(i-j)
        answer.append(cnt)
    return min(answer)

if __name__ == '__main__':
    real_answer = solution([3, 2, 1, 1, 2, 3, 1])
    print(real_answer)