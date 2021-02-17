# 방향은 북동남서
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
# 방향 바꿔주기
def change(d):
    if(d == 0):
        return 3
    elif(d == 1):
        return 0
    elif(d == 2):
        return 1
    elif(d == 3):
        return 2

def find(r,c,d):
    cnt = 1
    x, y = r, c
    arr[x][y] = 2 
    while(True):
        dc = d
        for _ in range(4):
            empty = 0
            dc = change(dc)
            nx, ny = x + dx[dc], y + dy[dc]
            # 유효 범위 안에 있고, 빈칸이라면
            if(0<=nx<n and 0<=ny<m and arr[nx][ny] == 0):
                cnt += 1
                x, y, d = nx, ny, dc
                arr[nx][ny] = 2
                empty = 1
                break
        # 4방향 모두 탐색 후 모든 칸이 청소가 되었다면
        if(empty == 0):
            # 후진
            if(d == 0):
                x += 1
            elif(d == 1):
                y -= 1
            elif(d == 2):
                x -= 1
            elif(d == 3):
                y += 1
            # 후진하려는 칸이 벽이라면 stop
            if(arr[x][y] == 1):
                break
    return cnt

n, m = map(int, input().split())
r, c, d = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
res = find(r,c,d)
print(res)