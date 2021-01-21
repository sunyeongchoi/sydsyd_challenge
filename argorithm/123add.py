T = int(input())


def dfs(n, number):
    global cnt
    if number == n:
        cnt += 1
        return 0
    elif number > n:
        return 0
    dfs(n, number+1)
    dfs(n, number+2)
    dfs(n, number+3)


for _ in range(T):
    cnt = 0
    n = int(input())
    dfs(n, 0)
    print(cnt)







