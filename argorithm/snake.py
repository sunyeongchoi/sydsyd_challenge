import sys
from collections import deque


# ----------- 입력 -----------
input = sys.stdin.readline
N = int(input())
K = int(input())
apples = [tuple(map(int, input().split(' '))) for _ in range(K)]
print(apples)
L = int(input())
rotate = []
for _ in range(L):
    X, C = tuple(input().strip(' ').split())
    rotate.append([int(X), C])
print(rotate)
# ----------------------------

# ---------- 기본 세팅 ----------
check = [[0]*(N+1) for _ in range(N+1)]
for y, x in apples:
    check[y][x] = 1     # 사과 자리 체크
dq = deque()  # 뱀
dq.append((1, 1))
dx, dy = 1, 0    # 나아갈 방향
t = 0   # 시간
k = 0   # rotate index
# -----------------------------
