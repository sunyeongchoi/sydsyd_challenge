def solution(grade):
    answer = []
    for fg in grade:
        cnt = 1
        for sg in grade:
            if fg < sg:
                cnt += 1
        answer.append(cnt)
    return answer

if __name__ == '__main__':
    real_answer = solution([2,2,1])
    print(real_answer)