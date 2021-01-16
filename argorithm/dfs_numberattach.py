n = int(input())
a = [list(map(int, input())) for _ in range(n)]

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
check = [[0]*n for _ in range(n)]
answer = []


def dfs(x, y):
    global cnt
    cnt += 1
    check[x][y] = 1

    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0 <= nx < n and 0 <= ny < n:
            if a[nx][ny] == 1 and check[nx][ny] == 0:
                dfs(nx, ny)


for i in range(n):
    for j in range(n):
        if a[i][j] == 1 and check[i][j] == 0:
            cnt = 0
            dfs(i, j)
            answer.append(cnt)

print(len(answer))
answer.sort()
print('\n'.join(map(str, answer)))

