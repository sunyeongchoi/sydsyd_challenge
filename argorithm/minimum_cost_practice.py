import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    distance = [sys.maxsize] * (N+1)
    distance[start] = 0
    while heap:
        weight, index = heapq.heappop(heap)
        for n, w in graph[index]:
            if distance[n] > weight + w:
                distance[n] = weight + w
                heapq.heappush(heap, (weight+w, n))
    return distance[end]


print(dijkstra(s, e))
