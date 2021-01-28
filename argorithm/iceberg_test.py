import sys
from collections import deque
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]
visited = [[False]*M for _ in range(N)]
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
division = False
answer = 0


def bfs(x, y):
    global arr
    global visited
    dq = deque()
    dq.append((x, y))
    visited[x][y] = True
    while dq:
        p_x, p_y = dq.popleft()
        for index in range(4):
            s_dx, s_dy = p_x+dx[index], p_y+dy[index]

            if 0 <= s_dx < N and 0 <= s_dy < M:
                if arr[s_dx][s_dy] == 0 and not visited[s_dx][s_dy]:
                    arr[p_x][p_y] -= 1
                    if arr[p_x][p_y] < 0:
                        arr[p_x][p_y] = 0

                if arr[s_dx][s_dy] > 0 and not visited[s_dx][s_dy]:
                    dq.append((s_dx, s_dy))
                    visited[s_dx][s_dy] = True


while not division:
    visited = [[False] * M for _ in range(N)]

    cnt = 0
    for i in range(N):
        for j in range(M):
            if arr[i][j] > 0 and not visited[i][j]:
                bfs(i, j)
                cnt += 1
    if cnt > 1:
        division = True
        print(answer)
        exit(0)

    if cnt < 1:
        print(0)
        exit(0)

    answer += 1

