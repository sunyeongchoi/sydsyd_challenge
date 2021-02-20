arr = list(map(int, input().split()))

sum = 0
for a in arr:
    sum += a**2
print(sum%10)