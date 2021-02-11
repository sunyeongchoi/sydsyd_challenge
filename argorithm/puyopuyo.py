from collections import deque

# BFS 함수
def bfs(x, y):
    queue = deque()
    temp = set()
    queue.append((x, y))

    while queue:
        qx, qy = queue.popleft()
        if (qx, qy) in temp:
            continue
        temp.add((qx, qy))
        for i in range(4):
            sx, sy = qx+dx[i], qy+dy[i]
            if not(0<=sx<n and 0<=sy<m):
                continue
            if arr[qx][qy] == arr[sx][sy]:
                queue.append((sx, sy))
    return temp

# 떨어뜨리는 함수
def fall():
    for i in range(n-1, -1, -1):
        for j in range(m):
            if arr[i][j] == '.':
                for s in range(i-1, -1, -1):
                    if arr[s][j] != '.':
                        arr[i][j] = arr[s][j]
                        arr[s][j] = '.'
                        break


# 메인 함수
if __name__ == '__main__':
    answer = 0
    n, m = 12, 6
    arr = list(list(input()) for _  in range(12))
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    
    while True:
        check = 0
        for i in range(n):
            for j in range(m):
                if arr[i][j]=='.': continue
                result = bfs(i, j)
                if len(result) >= 4:
                    if check == 0: 
                        check = 1
                    for x, y in result:
                        arr[x][y] = '.'
        fall()
        if check == 1:  
            answer += 1
        else:
            break
    print(answer)

