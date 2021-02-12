N, X = map(int, input().split())
arr = list(map(int, input().split()))

[print(a, end=' ') for a in list(filter(lambda x: x < X, arr))]