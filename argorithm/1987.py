import sys
input = sys.stdin.readline

def dfs(arr, x, y, visited):
    global answer
    answer = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited.add(arr[x][y])
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if not(0<=nx<r and 0<=ny<c):
            continue
        if not arr[nx][ny] in visited:
            answer += 1
            dfs(arr, nx, ny, visited)


r, c = map(int, input().split())
arr = [list(input().strip()) for _ in range(r)]
visited = set()

for i in range(r):
    for j in range(c):
        if not arr[i][j] in visited:
            dfs(arr, i, j, visited)

print(answer)