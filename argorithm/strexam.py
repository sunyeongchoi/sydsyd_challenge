def solution(s):
    if len(s) ==4 or len(s)==6:
        for i in range(len(s)):
            if not s[i].isdigit():
                return False
        return True
    else:
        return False


if __name__ == '__main__':
    real_answer = solution('a234')
    print('정답 : ', real_answer)
