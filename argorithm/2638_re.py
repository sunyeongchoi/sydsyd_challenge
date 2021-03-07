import sys
sys.setrecursionlimit(10**6)
input = sys.stdin.readline

# 변수 초기화
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

def dfs(x, y):
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<m and not visited[nx][ny]:
            if arr[nx][ny] != 0:
                arr[nx][ny] += 1
            else:
                visited[nx][ny]=1
                dfs(nx, ny)

def remove():
    for i in range(n):
        for j in range(m):
            if arr[i][j] >= 3:
                arr[i][j] = 0
            elif arr[i][j] == 2:
                arr[i][j] = 1

def check():
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                return False
    return True

while True:
    if check():
        print(answer)
        break
    visited = [[0]*m for _ in range(n)]
    dfs(0, 0)
    remove()
    visited[0][0] = 1
    answer += 1