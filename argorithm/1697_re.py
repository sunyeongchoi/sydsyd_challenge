from collections import deque
import sys
input = sys.stdin.readline

def bfs(n):
    queue = deque([n])
    while queue:
        x = queue.popleft()
        if x == k:
            return visited[x]
        for nx in [x-1, x+1, 2*x]:
            if 0<=nx<=MAX and not visited[nx]:
                visited[nx]=visited[x]+1
                queue.append(nx)


n, k = map(int, input().split())
MAX =10**5
visited = [0]*(MAX+1)
print(bfs(n))