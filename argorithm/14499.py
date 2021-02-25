import sys
input = sys.stdin.readline

N, M, x, y, cnt = map(int, input().split())

map_list = [list(map(int, input().split())) for _ in range(N)]
move_list = list(map(int, input().split()))
dice = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
dx, dy = [0, 0, -1, 1], [1, -1, 0, 0]
for m in move_list:
    # 범위
    sx, sy = x+dx[m-1], y+dy[m-1]
    if not(0<=sx<N and 0<=sy<M):
        continue

    # 주사위 굴리기
    if m==1: # 동
        dice[4], dice[1], dice[3], dice[6] = dice[6], dice[4], dice[1], dice[3]
    elif m==2: # 서
        dice[4], dice[1], dice[3], dice[6] = dice[1], dice[3], dice[6], dice[4]
    elif m==3: # 남
        dice[2], dice[1], dice[5], dice[6] = dice[1], dice[5], dice[6], dice[2]
    else: # 북
        dice[2], dice[1], dice[5], dice[6] = dice[6], dice[2], dice[1], dice[5]
    
    # 복사
    if map_list[sx][sy] == 0:
        map_list[sx][sy] = dice[6]
    else:
        dice[6] = map_list[sx][sy]
        map_list[sx][sy] = 0

    x, y = sx, sy
    print(dice[1])