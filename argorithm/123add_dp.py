import sys

T = int(sys.stdin.readline())

dp = [0, 1, 2, 4]

for _ in range(T):
    N = int(sys.stdin.readline())
    for i in range(len(dp), N+1):
        print(i)
        dp.append(dp[i-1] + dp[i-2] + dp[i-3])
    print(dp)
    sys.stdout.write(str(dp[N]) + "\n")
