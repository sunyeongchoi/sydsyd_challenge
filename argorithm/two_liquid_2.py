import sys
input = sys.stdin.readline

N = int(input())
arr = sorted(list(map(int, input().split())))

start = 0
end = len(arr)-1

min = sys.maxsize
while start < end:
    calc = arr[start] + arr[end]
    if abs(calc) < min:
        min = abs(calc)
        answer = arr[start], arr[end]
    if calc == 0:
        break
    if calc < 0:
        start += 1
    else:
        end -= 1

for i in sorted(answer):
    print(i, end=' ')
