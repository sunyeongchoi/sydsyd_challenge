import sys; input=sys.stdin.readline
from collections import defaultdict

n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(m)]
graph = defaultdict(list)
for a in arr:
    graph[a[0]].append(a[1])

def dfs():
    pass


