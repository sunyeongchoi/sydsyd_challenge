def pop_num(b, m, n):
    pop_set = set()
    # search
    for i in range(1, n):
        for j in range(1, m):
            if b[i][j] == b[i - 1][j - 1] == b[i - 1][j] == b[i][j - 1] != '_':
                pop_set |= {(i, j), (i - 1, j - 1), (i - 1, j), (i, j - 1)}
    print(pop_set)
    # set_board
    for i, j in pop_set:
        b[i][j] = 0
    for i, row in enumerate(b):
        print(row)
        empty = ['_'] * row.count(0)
        print(empty)
        b[i] = empty + [block for block in row if block != 0]
        print(b[i])
    return len(pop_set)


def solution(m, n, board):
    count = 0
    b = list(map(list, zip(*board)))
    print(b)
    while True:
        pop = pop_num(b, m, n)
        if pop == 0:
            return count
        count += pop


if __name__ == '__main__':
    answer = solution(4, 5, ['CCBDE', 'AAADE', 'AAABF', 'CCBBF'])
    print('출력값: ', answer)
