arr = [int(input().rstrip()) for _ in range(10)]

answer = set()
for a in arr:
    answer.add(a%42)

print(len(answer))
