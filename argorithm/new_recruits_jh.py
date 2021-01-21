import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    cnt = 1
    N = int(input())
    grades = sorted([tuple(map(int, input().split())) for _ in range(N)], key=lambda x: x[0])
    for idx, val in enumerate(grades[:N-1]):
        if val[1] < grades[idx+1][1]:
            cnt += 1
    print(cnt)
