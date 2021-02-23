N = int(input())
arr = [list(map(int, input().split())) for _ in range(N)]

answer = sorted(arr, key=lambda x: (x[0], x[1]))

for a, b in answer:
    print(a, b)