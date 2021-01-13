from collections import deque

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]


def dfs(cnt, x, y):
    q.append([x, y])
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0 <= nx < n and 0 <= ny < n:
                if a[nx][ny] == 1:
                    q.append([nx, ny])
                    cnt += 1
                    a[nx][ny] = 0
    return cnt


n = int(input())
a = [list(map(str, input())) for _ in range(n)]
q = deque()

cnt = 0
answer = 0

for i in range(n):
    for j in range(n):
        if a[i][j] == 1:
            answer = dfs(i, j)

print(answer)
