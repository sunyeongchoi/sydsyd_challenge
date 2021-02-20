# 나이가 증가하는 순으로, 나이가 같으면 먼저 가입한 사람이 앞에 오는 순서
N = int(input())
arr = [input().split() for _ in range(N)]

result = sorted(arr, key=lambda x: int(x[0]))

for r in result:
    print(' '.join(r))