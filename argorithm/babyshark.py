import sys
import heapq
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().split())) for _ in range(N)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
heap = []


def init():
    for i in range(N):
        for j in range(N):
            if graph[i][j] == 9:
                heapq.heappush(heap, (0, i, j))
                graph[i][j] = 0
                return


def bfs():
    baby_shark_size, baby_shark_cnt, answer = 2, 0, 0
    visited = [[False]*N for _ in range(N)]
    while heap:
        cnt, q_x, q_y = heapq.heappop(heap)
        if 0 < graph[q_x][q_y] < baby_shark_size:
            baby_shark_cnt += 1
            graph[q_x][q_y] = 0
            if baby_shark_size == baby_shark_cnt:
                baby_shark_size += 1
                baby_shark_cnt = 0
            answer += cnt
            cnt = 0
            while heap:
                heap.pop()
            visited = [[False]*N for _ in range(N)]
        for i in range(4):
            s_x, s_y = q_x+dx[i], q_y+dy[i]
            if 0 <= s_x < N and 0 <= s_y < N:
                if graph[s_x][s_y] > baby_shark_size or visited[s_x][s_y]:
                    continue
                heapq.heappush(heap, (cnt+1, s_x, s_y))
                visited[s_x][s_y] = True
    print(answer)


init()
bfs()





