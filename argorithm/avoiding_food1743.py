import sys
from collections import deque
input = sys.stdin.readline

def bfs(x, y):
    q = deque()
    cnt = 1
    q.append((x, y))
    cnt = set()
    while q:
        qx, qy = q.popleft()
        cnt.add((qx, qy))
        if (qx, qy) in visited:
            continue
        visited.add((qx, qy))
        for i in range(4):
            sx, sy = qx+dx[i], qy+dy[i]
            if not(0<=sx<N and 0<=sy<M):
                continue
            if arr[sx][sy] == arr[qx][qy]:
                q.append((sx, sy))
    return len(cnt)

if __name__ == '__main__':
    N, M, RC = map(int, input().split())
    arr = [[0]*M for _ in range(N)]
    for _ in range(RC):
        r, c = map(int, input().split())
        arr[r-1][c-1] = 1
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    visited = set()
    answer = []

    for i in range(N):
        for j in range(M):
            if arr[i][j] != 0 and (i, j) not in visited:
                count = bfs(i, j)
                answer.append(count)
    print(max(answer))
