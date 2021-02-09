import sys
input = sys.stdin.readline

n = int(input())
dp = [0]
dp += list(int(input()) for _ in range(n))
answer = [0]*(n+1)

for i in range(1, n+1):
    if i == 1:
        answer[i] = dp[i]
    elif i == 2:
        answer[i] = dp[i-1]+dp[i]
    else:
        answer[i] = max(answer[i-1], answer[i-3]+dp[i-1]+dp[i], answer[i-2]+dp[i])
print(answer[-1])
