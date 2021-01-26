import sys
import heapq

input = sys.stdin.readline
N = int(input())
M = int(input())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s_node, e_node, cost = map(int, input().split())
    graph[s_node].append((e_node, cost))
s, e = map(int, input().split())

distance = [sys.maxsize]*(N+1)


def dijkstra(start, end):
    heap = []
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        h_cost, h_node = heapq.heappop(heap)
        if distance[h_node] < h_cost:
            continue
        for n, c in graph[h_node]:
            sum_cost = h_cost + c
            if distance[n] > sum_cost:
                distance[n] = sum_cost
                heapq.heappush(heap, (sum_cost, n))
    return distance[end]


print(dijkstra(s, e))



