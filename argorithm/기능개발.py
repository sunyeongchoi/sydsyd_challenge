import math

def solution(progresses, speeds):
    answer = []
    temp = []
    for index, p in enumerate(progresses):
        val = math.ceil((100-p)/speeds[index])
        temp.append(val)
    
    k = 0
    for i in range(len(temp)):
        if temp[i] > temp[k]:
            answer.append(i-k)
            k=i
    answer.append(len(temp)-k)
    return answer

if __name__ == '__main__':
    result = solution([93, 30, 55], [1, 30, 5])
    print(result)