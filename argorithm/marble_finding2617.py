from collections import defaultdict

def dfs(node, weight):
    global cnt
    visited[node] = True
    for n in weight[node]:
        if not visited[n]:
            cnt += 1
            dfs(n, weight)
    return cnt

if __name__ == '__main__':    
    N, M = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(M)]
    result = 0

    light = defaultdict(list)
    heavy = defaultdict(list)

    for x, y in arr:
        heavy[x].append(y)
        light[y].append(x)

    for i in range(1, N+1):
        visited = [False]*(N+1)
        cnt = 0
        if dfs(i, heavy) >= (N+1)//2:
            result += 1
        cnt = 0
        if dfs(i, light) >= (N+1)//2:
            result += 1
    print(result)