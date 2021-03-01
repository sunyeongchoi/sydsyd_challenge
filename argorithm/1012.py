import sys
sys.setrecursionlimit(10000)
input = sys.stdin.readline

def dfs(arr, visited, x, y):
    dx = [0, 0, -1, 1]
    dy = [-1, 1, 0, 0]

    visited[x][y] = True
    for i in range(4):
        sx, sy = x+dx[i], y+dy[i]
        if 0<=sx<n and 0<=sy<m and not visited[sx][sy] and arr[sx][sy]==1:
            dfs(arr, visited, sx, sy)

t = int(input())
for _ in range(t):
    m, n, k = map(int, input().split())
    arr = [[0]*m for _ in range(n)]
    for _ in range(k):
        a, b = map(int, input().split())
        arr[b][a]=1
    
    answer = 0
    visited = [[False]*m for _ in range(n)]
    for x in range(n):
        for y in range(m):
            if not visited[x][y] and arr[x][y]==1:
                dfs(arr, visited, x, y)
                answer += 1
    print(answer)