import sys
import heapq
input = sys.stdin.readline

N, M, X = map(int, input().split())
graph = [[] for _ in range(N+1)]
for i in range(M):
    s_node, e_node, cost = map(int, input().split())
    graph[s_node].append((e_node, cost))


def dijkstra(start, end):
    heap = []
    distance = [sys.maxsize] * (N + 1)
    heapq.heappush(heap, (0, start))
    distance[start] = 0
    while heap:
        h_cost, h_node = heapq.heappop(heap)
        for n, c in graph[h_node]:
            sum_cost = h_cost + c
            if distance[n] > sum_cost:
                distance[n] = sum_cost
                heapq.heappush(heap, (sum_cost, n))
    return distance[end]


result = []
for i in range(N):
    result.append(dijkstra(i+1, X)+dijkstra(X, i+1))
print(max(result))
