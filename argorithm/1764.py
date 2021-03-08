import sys
input = sys.stdin.readline

n, m = map(int, input().split())

no_listen_arr = set(input().strip() for _ in range(n))
no_see_arr = set(input().strip() for _ in range(m))

answer = no_listen_arr&no_see_arr
print(len(answer))
[print(i) for i in sorted(list(answer))]