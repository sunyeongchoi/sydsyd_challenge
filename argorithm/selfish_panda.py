import sys
input = sys.stdin.readline

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]
temp = 0


def dfs(a, t, i, j):
    visited[i][j] = True
    a[i][j]
    pass


while True:
    visited = [[False] * n for _ in range(n)]
    for i_i, i in enumerate(arr):
        for i_j, j in enumerate(arr):
            if not visited[i_i][i_j] and arr[i_i][i_j] > temp:
                dfs(arr, temp, i_i, i_j)