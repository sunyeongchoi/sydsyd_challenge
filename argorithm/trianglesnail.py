def solution(n):
    answer = []
    triangle = [[0] * n for _ in range(n)]
    num = 1
    x, y = -1, 0

    for i in range(n):
        for j in range(i, n):
            if i % 3 == 0:
                x += 1
            elif i % 3 == 1:
                y += 1
            elif i % 3 == 2:
                x -= 1
                y -= 1
            triangle[x][y] = num
            num += 1
    for tri in triangle:
        for t in tri:
            if t != 0:
                answer.append(t)
    return answer


if __name__ == '__main__':
    real_answer = solution(4)
    print('정답 : ', real_answer)
