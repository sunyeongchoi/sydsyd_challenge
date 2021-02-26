def solution(A, B):
    temp = []
    if len(A)<len(B): temp = B; B = A; A = temp
    A.sort()
    B.sort()
    i = 0
    for a in A:
        if i < len(B) - 1 and B[i] < a:
            i += 1
        if a == B[i]:
            return a
    return -1

if __name__ == '__main__':
    real_answer = solution([1,3,2,5],[4,4,4,4,4,5])
    print(real_answer)