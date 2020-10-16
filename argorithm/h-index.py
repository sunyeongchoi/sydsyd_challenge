def solution(citations):
    answer = []
    cnt = 0
    for i in range(len(citations)):
        for j in range(len(citations)):
            if citations[i] <= citations[j]:
                cnt += 1
        if citations[i] >= cnt:
            answer.append(cnt)
        cnt = 0
    return max(answer)


if __name__ == '__main__':
    real_answer = solution([3, 0, 6, 1, 5])
    print(real_answer)
    
#“나머지 논문이 h번 이하 인용되었다면” 이라는 조건까지 따져보면, 이 조건까지 추가해주자
