def dfs(node, depth):
    visited[node] = True
    for n in graph[node]:
        dfs(n, depth+1)
    cnt[node] = depth

if __name__ == '__main__':    
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    graph = [[] for _ in range(N+1)]
    visited = [False]*(N+1)
    cnt = [0]*(N+1)

    for x, y in arr:
        graph[x].append(y)

    for i in range(1, N+1):
        if not visited[i]:
            dfs(i, 0)
    print(cnt)
    print(max(cnt))

