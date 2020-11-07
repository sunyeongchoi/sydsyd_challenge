def solution(s, op):
    answer = []
    s_list = list(s)
    for i in range(len(s_list)-1):
        s_left = int(''.join(map(str, s_list[:i+1])))
        print('s_left : ', s_left)
        s_right = int(''.join(map(str, s_list[i+1:])))
        print('s_right : ', s_right)
        answer.append(s_left + s_right)
    return answer


if __name__ == '__main__':
    real_answer = solution('1234','+')
    print(real_answer)