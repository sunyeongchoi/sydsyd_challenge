from collections import deque
import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = []

def bfs(x, y):
    q = deque()
    q.append((x, y))
    visited = [[-1]*m for _ in range(n)]
    visited[x][y]=0
    while q:
        x, y = q.popleft()
        for i in range(4):
            sx, sy = x+dx[i], y+dy[i]
            if not (0<=sx<n and 0<=sy<m):
                continue
            if arr[sx][sy]=='L' and visited[sx][sy]==-1:
                visited[sx][sy] = visited[x][y]+1
                q.append((sx, sy))
    return max([max(val) for val in visited])


for a in range(n):
    for b in range(m):
        if arr[a][b]=='L':
            if 0<=a-1 and a+1<n:
                if arr[a-1][b]=='L' and arr[a+1][b]=='L':
                    continue
            if 0<=b-1 and b+1<m:
                if arr[a][b-1]=='L' and arr[a][b+1]=='L':
                    continue
            answer.append(bfs(a, b))

print(max(answer))


