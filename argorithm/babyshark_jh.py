import sys
from collections import deque
import heapq
input = sys.stdin.readline
N = int(input())
graph=[]
for i in range(N):
    row = list(map(int, input().split()))
    for j in range(N):
       if row[j]==9:
           start = (i,j,0)
    graph.append(row)
print(graph)
dx=[-1,1,0,0]
dy=[0,0,-1,1]


def bfs(start,graph,shark_size):
    queue = deque()
    queue.append(start)
    x,y,t=start
    graph[x][y] = 0
    visited = set()
    result = []
    while queue:
        x,y,t = queue.popleft()
        visited.add((x,y))
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<N and 0<=ny<N and (nx,ny) not in visited:
                visited.add((nx,ny))
                if graph[nx][ny]==0 or graph[nx][ny]==shark_size:
                    queue.append((nx,ny,t+1))
                    continue
                if graph[nx][ny] > shark_size:
                    continue
                else:
                    heapq.heappush(result,(t+1,nx,ny))
    if result:
        return result[0]
    return False
time = 0
shark_size = 2
eated = 0
while True:
    eating_fish = bfs(start,graph,shark_size)
    if not eating_fish:break
    t,nx,ny = eating_fish
    time += t
    eated += 1
    if eated == shark_size:
        shark_size+=1
        eated=0
    start = (nx,ny,0)
print(time)