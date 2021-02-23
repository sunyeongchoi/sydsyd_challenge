# x, y를 함께 min 고려해주는 이유는 x, y좌표를 기준으로 w, h까지의 거리와
# (0, 0)까지의 거리를 고려해야하기 때문입니다.
# 예시 = (1 2 5 4) 이면 답은 1이어야 합니다.

x, y, w, h = map(int, input().split())

print(min(x, y, w-x, h-y))