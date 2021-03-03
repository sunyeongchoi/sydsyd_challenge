def solution(new_id):
    answer = []
    new_id = new_id.lower()
    for i in new_id:
        if i=='-' or i=='_' or i=='.' or i.isalnum():
            answer.append(i)

    try:
        while True:
            check = 0
            if answer[0]=='.':
                answer = answer[1:]
                check = 1
            if answer[-1]=='.':
                answer = answer[:-1]
                check = 1
            for a in range(len(answer)-1):
                if answer[a]=='.' and answer[a+1]=='.':
                    check = 1
                    answer = answer[:a]+answer[a+1:]
                    break
            if not check:
                break
    except:
        pass

    if len(answer)==0:
        answer = 'a'
    if len(answer)>15:
        answer = answer[:15]
        if answer[-1]=='.':
            answer = answer[:-1]
    if len(answer)<3:
        answer += answer[-1] * (3-len(answer))
    return ''.join(answer)

if __name__ == '__main__':
    print(solution("=.="))