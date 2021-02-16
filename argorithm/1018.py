import sys
input = sys.stdin.readline

N, M = map(int, input().split())
arr = [list(input().rstrip()) for _ in range(N)]
answer = []

for i in range(N-7):
    for j in range(M-7):
        cnt1, cnt2 = 0, 0
        for a in range(i, i+8):
            for b in range(j, j+8):
                if (a+b)%2 == 0:
                    if arr[a][b] != 'W': cnt1 += 1
                    if arr[a][b] != 'B': cnt2 += 1
                else:
                    if arr[a][b] != 'B': cnt1 += 1
                    if arr[a][b] != 'W': cnt2 += 1
        answer.append(cnt1)
        answer.append(cnt2)
print(min(answer))
