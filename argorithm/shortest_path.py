import sys
import heapq
input = sys.stdin.readline

V, E = map(int, input().split())
K = int(input())
distance = [sys.maxsize]*(V+1)
arr = [list(map(int, input().split())) for _ in range(E)]
graph = [[] for _ in range(V+1)]
for start, end, cost in arr:
    graph[start].append((cost, end))
heap = []


def dijkstra(s_node):
    heapq.heappush(heap, (0, s_node))
    distance[s_node] = 0
    while heap:
        h_cost, h_node = heapq.heappop(heap)
        if h_cost > distance[h_node]:
            continue
        for c, e in graph[h_node]:
            sum_cost = h_cost+c
            if sum_cost < distance[e]:
                distance[e] = sum_cost
                heapq.heappush(heap, (sum_cost, e))


dijkstra(K)
for i in range(1, V+1):
    print('INF' if distance[i] == sys.maxsize else distance[i])