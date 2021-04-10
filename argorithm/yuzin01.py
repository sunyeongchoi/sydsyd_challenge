import sys
sys.setrecursionlimit(10000)

def dfs(x,y):
    dx = [1, -1, 0, 0]
    dy = [0, 0, 1, -1]

    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < N and ny >= 0 and ny < M:
            if graph[nx][ny] == 1:
                graph[nx][ny] = 0
                dfs(nx, ny)


t = int(input())
# m: 열   n: 행
for _ in range(t):
    M, N, K = map(int, input().split())
    graph = [[0] * M for _ in range(N)]
    result = 0

    for _ in range(K):
        m, n = map(int, input().split())
        graph[n][m] = 1  # IndexError: list index out of range 실수 조심
    print(graph)
    for i in range(N):
        for j in range(M):
            print('hey')
            if graph[i][j] > 0:
                print('why')
                dfs(i,j)
                result += 1

    print(result)