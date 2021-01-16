from collections import deque, Counter
from functools import reduce

n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = [[0]*n for _ in range(n)]


def bfs(x, y, cnt):
    q = deque()
    q.append([x, y])
    check[x][y] = cnt
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx, ny = x + dx[i], y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1 and check[nx][ny] == 0:
                    q.append([nx, ny])
                    check[nx][ny] = cnt


cnt = 0
for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and check[i][j] == 0:
            cnt += 1
            bfs(i, j, cnt)
print(cnt)
print('------------------------------')
print(check)
print('------------------------------')
answer = reduce(lambda x, y: x+y, check)
print(answer)
print('------------------------------')
answer = [x for x in answer if x > 0]
print(answer)
print('------------------------------')
answer = sorted(list(Counter(answer).values()))
print('\n'.join(map(str, answer)))
print('------------------------------')
