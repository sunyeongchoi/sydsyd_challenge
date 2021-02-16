import heapq
import sys
input = sys.stdin.readline

def dijkstra(start, end):
    heap = []
    distance = [[sys.maxsize]*(M) for _ in range(N)]

    sx, sy = start
    ex, ey = end

    heapq.heappush(heap, (0, sx, sy))
    distance[sx][sy] = 0

    while heap:
        weight, hsx, hsy = heapq.heappop(heap)
        for i in range(4):
            hx, hy = hsx+dx[i], hsy+dy[i]
            if not(0<=hy<M and 0<=hx<N):
                continue
            if distance[hx][hy] > weight+arr[hx][hy]:
                distance[hx][hy] = weight+arr[hx][hy]
                heapq.heappush(heap, (weight+arr[hx][hy], hx, hy))
    
    return distance[ex][ey]

if __name__ == '__main__':
    M, N = map(int, input().split())
    arr = [list(map(int, input().rstrip())) for _ in range(N)]
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]

    print(dijkstra((0, 0), (N-1, M-1)))
