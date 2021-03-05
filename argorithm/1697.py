from collections import deque
import sys
input = sys.stdin.readline


def bfs(n):
    count = 0
    queue = deque([(n, count)])
    while queue:
        val, cnt = queue.popleft()
        count = cnt
        if not visited[val]:
            visited[val]=1
        if val == k:
            return count
        count += 1
        if val-1 >= 0:
            queue.append((val-1, count))
        if val+1 <= 100000:
            queue.append((val+1, count))
        if val*2 <= 100000:
            queue.append((val*2, count))
    return count

n, k = map(int, input().split())
visited = [0]*100001
print(bfs(n))
