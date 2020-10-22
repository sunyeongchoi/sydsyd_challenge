def solution(land):
    answer_arr = []
    for i in range(0, len(land)):
        first = land[0][i]
        print('set(land[1])', set(land[1]))
        print('set(land[1]) - set(map(int, list(str(land[1][i]))))', set(land[1]) - set(map(int, list(str(land[1][i])))))
        second = max(set(land[1]) - set(map(int, list(str(land[1][i])))))
        print('set(land[2])', set(land[2]))
        print('set(land[2]) - set(map(int, list(str(land[2][i]))))', set(land[2]) - set(map(int, list(str(land[2][i])))))
        temp = land[2].index(second)
        print('temp', temp)
        third = max(set(land[2]) - set(map(int, list(str(land[2][temp])))))
        answer = first + second + third
        answer_arr.append(answer)
    #print('answer_arr', answer_arr)
    return max(answer_arr)


if __name__ == '__main__':
    real_answer = solution([[9, 5, 2, 3], [9, 8, 6, 7], [8, 9, 7, 1], [100, 9, 8, 1]])
    print(real_answer)

