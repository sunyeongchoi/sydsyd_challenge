# 500번을 반복해도 1이 되지 않는다면 –1을 반환해 주세요.
def solution(num):
    answer = 0
    while num != 1:
        if num % 2 == 0:
            num /= 2
            answer += 1
        else:
            num = num*3 + 1
            answer += 1
    if answer >= 500:
        return -1
    return answer


if __name__ == '__main__':
    real_answer = solution(6)
    print('정답 : ', real_answer)
