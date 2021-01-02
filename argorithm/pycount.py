def solution(s):
    pcount = 0
    ycount = 0
    for i in range(len(s)):
        if s[i].upper() == 'P':
            pcount += 1
        elif s[i].upper() == 'Y':
            ycount += 1
    if pcount == ycount:
        return True
    else:
        return False


if __name__ == '__main__':
    real_answer = solution('Pyy')
    print('정답 : ', real_answer)
