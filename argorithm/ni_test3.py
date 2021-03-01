def solution(A):
    answer = 0
    temp = []
    for i in range(len(A)-1):
        temp.append(A[i]-A[i+1])

    t1 = temp[0]
    for j in enumerate(temp):
        if t1==j:
            


    return answer

if __name__ == '__main__':
    real_answer = solution([-1,1,3,3,3,2,3,2,1,0])
    
    print(real_answer)