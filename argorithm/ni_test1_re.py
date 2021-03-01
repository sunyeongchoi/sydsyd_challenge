def solution(A):
    A = list(str(A))
    if '-' in A:
        A = A[1:]
        answer = ['-']
        for i, a in enumerate(A):
            if int(a) > 5:
                answer += ['5']
                answer += A[i:]
                return int(''.join(answer))
            else:
                answer.append(a)
    else:
        answer = []
        for i, a in enumerate(A):
            if int(a) < 5:
                answer.append('5')
                answer+= A[i:]
                return int(''.join(answer))
            else:
                answer.append(a)
    return int(''.join(answer))

if __name__ == '__main__':
    real_answer = solution(268)
    print(real_answer)