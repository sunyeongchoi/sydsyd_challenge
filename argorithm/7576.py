import sys; input=sys.stdin.readline
from collections import deque

m, n = map(int, input().split())

def bfs(queue, arr):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    while queue:
        x, y, cnt = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not(0<=nx<n and 0<=ny<m):
                continue
            if arr[nx][ny]==0:
                arr[nx][ny]=1
                queue.append((nx, ny, cnt+1))
    return cnt

def check(answer, arr):
    for i in range(n):
        for j in range(m):
            if arr[i][j]==0:
                return -1
    return answer


arr = [list(map(int, input().split())) for _ in range(n)]
queue = deque()
answer = 0
for i in range(n):
    for j in range(m):
        if arr[i][j]==1:
            # 여기가 이 문제의 포인트!!!
            # 처음에 익은 토마토가 한군데만이 아니라 다른데도 있을시에 동시에 큐에 넣어줌으로써 동시에 서로 다른 토마토가 다른 위치에서 익히도록 한다.
            queue.append((i, j, answer))
answer = bfs(queue, arr)
print(check(answer, arr))