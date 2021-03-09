import sys
input = sys.stdin.readline

n, l, r = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]

def dfs(arr, visited, x, y):
    visited[x][y]=1
    for i in range(4):
        nx, ny = x+dx[i], y+dy[i]
        if 0<=nx<n and 0<=ny<n and not visited[nx][ny]:
            if l<= abs(arr[x][y]-arr[nx][ny]) <=r:
                temp.append((nx, ny))
                dfs(arr, visited, nx, ny)
    return temp

answer=0
while True:
    visited = [[0]*n for _ in range(n)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    result = 0
    
    for a in range(n):
        for b in range(n):
            temp = []
            if not visited[a][b]:
                t = dfs(arr, visited, a, b)
                result += len(t)
                answer += 1

                if len(t)>0:
                    sum = 0
                    for x, y in t:
                        sum += arr[x][y]
                    avg = sum/len(t)

                    for i, j in t:
                        arr[i][j] = int(avg)
    print(result)
        
    if result == 0:
        print(answer)
        exit(0)
                


