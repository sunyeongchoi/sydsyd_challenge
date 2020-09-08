from numpy import median


def solution(brown, yellow):
    s_answer = []
    # yellow의 약수 구하기
    yak_list = [int(i) for i in range(1, yellow+1) if yellow % i == 0]
    if len(yak_list) % 2 == 0:
        while len(yak_list):
            x = yak_list.pop()
            y = yak_list.pop(0)
            if (x+2)*(y+2)-(x*y) == brown:
                s_answer.append(int(x+2))
                s_answer.append(int(y+2))
                return s_answer
    else:
        while len(yak_list):
            if len(yak_list) == 1:
                x = median(yak_list)
                y = x
            else:
                x = yak_list.pop()
                y = yak_list.pop(0)
            if (x+2)*(y+2)-(x*y) == brown:
                s_answer.append(int(x+2))
                s_answer.append(int(y+2))
                return s_answer


if __name__ == '__main__':
    answer = solution(8, 1)
    print('출력값: ', answer)
