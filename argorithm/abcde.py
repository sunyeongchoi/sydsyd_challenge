import sys

N, M = map(int, input().split())
arr = [[] for _ in range(N)]
visited = [False] * N

# 그래프를 인접 리스트 방식으로 담는다.
for _ in range(M):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    arr[a].append(b)
    arr[b].append(a)


# dfs 깊이가 4이면 return 1
def dfs(n, depth):
    visited[n] = True

    if depth >= 4:
        print(1)
        exit(0)

    for k in arr[n]:
        if not visited[k]:
            dfs(k, depth+1)
            visited[k] = False


for i in range(N):
    if not visited[i]:
        dfs(i, 0)
        visited[i] = False

print(0)
