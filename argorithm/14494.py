import sys
input = sys.stdin.readline

n, m = map(int, input().split())
d = [[-1]*(m+1) for _ in range(n+1)]

# n, m에서 왼쪽, 왼쪽위, 위 방향으로 이동하면서 1, 1에 도착했을때의 개수를 더한다.
def dp(n, m):
    if n==0 or m==0:
        return 0
    if n==1 and m==1:
        return 1
    if d[n][m]!=-1:
        return d[n][m]
    result = (dp(n,m-1)+dp(n-1,m)+dp(n-1,m-1))%1000000007
    d[n][m] = result
    return result

print(dp(n, m)%1000000007)
