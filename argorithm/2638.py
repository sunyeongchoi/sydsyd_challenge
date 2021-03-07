import sys
input = sys.stdin.readline

# 변수 초기화
n, m = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(n)]
dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
answer = 0

# 치즈 녹이는 함수
def cheese():
    temp = []
    for x in range(n):
        for y in range(m):
            if arr[x][y]==1:
                cnt = 0
                for k in range(4):
                    nx, ny = x+dx[k], y+dy[k]
                    if 0<=nx<n and 0<=ny<m and arr[nx][ny]==0: cnt += 1
                if cnt >= 2:
                    arr[x][y] = 2
                    temp.append((x, y))
    return temp


while True:
    # 아직 안녹은 치즈가 있는지 확인
    s = 0
    for i in range(n):
        for j in range(m):
            if arr[i][j]==1:
                s += 1
    # 치즈가 다 녹았다면 answer 출력
    if s==0:
        print(answer)
        break
    
    # 
    result = cheese()
    answer += 1
    for r, c in result:
        arr[r][c] = 0
    