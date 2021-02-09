import sys
input = sys.stdin.readline

N = int(input())
nums = list(map(int, input().split()))

min = 1000000
max = -1000000

for num in nums:
    if num <= min:
        min = num
for num in nums:
    if num >= max:
        max = num
print(f'{min} {max}')