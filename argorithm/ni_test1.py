def solution(A):
    answer = ''

    if A < 0:
        A = str(abs(A))
        A_list = list(str(abs(A)))

        for i, n in enumerate(A_list):
            if int(n) > 5:
                answer+='5'
                answer+=A[i:]
                return int(answer)
            else:
                answer+=n
    else:
        A = str(A)
        A_list = list(str(A))
        for i, n in enumerate(A_list):
            if int(n) < 5:
                answer+='5'
                answer+=A[i:]
                return int(answer)
            else:
                answer+=n
    return int(answer)

if __name__ == '__main__':
    real_answer = solution(-999)
    print(real_answer)