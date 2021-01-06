def solution(s):
    answer = ''

    # 공백을 기준으로 나눔
    words = s.split(' ')

    # 짝수는 대문자, 홀수는 소문자
    for word in words:
        for index in range(len(word)):
            if index % 2 == 0:
                answer += word[index].upper()
            else:
                answer += word[index].lower()
        answer += ' '
    
    # 리턴
    return answer[:-1]


if __name__ == '__main__':
    real_answer = solution('try hello world')
    print('정답 : ', real_answer)
