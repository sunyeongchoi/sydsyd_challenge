import sys
input = sys.stdin.readline

N, K = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(N)]

dp = [[0]*(K+1) for _ in range(N+1)]

for row in range(1, N+1):
    wi, vi = arr[row-1]
    for col in range(1, K+1):
        if wi <= col:
            dp[row][col] = max(vi+dp[row-1][col-wi], dp[row-1][col])
        else:
            dp[row][col] = dp[row-1][col]
print((dp[-1][-1]))