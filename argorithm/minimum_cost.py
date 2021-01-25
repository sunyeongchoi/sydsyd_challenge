import sys
from heapq import heappush, heappop

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N + 1)]
for i in range(M):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
s, e = map(int, input().split())


def dijkstra(start, end):
    heap = []
    heappush(heap, (0, start))  # 시작 지점 힙에 추가
    distance = [sys.maxsize] * (N+1)    # 각 정점사이의 거리 무한대로 초기화
    distance[start] = 0     # 시작 지점 0으로 초기화
    while heap:
        weight, index = heappop(heap)
        for e, c in graph[index]:
            if distance[e] > weight + c:
                distance[e] = weight + c
                heappush(heap, (weight+c, e))
        print(distance)
    return distance[end]


print(dijkstra(s, e))
