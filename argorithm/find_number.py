import sys
input = sys.stdin.readline

N = int(input())
AN = list(map(int, input().split()))
M = int(input())
MN = list(map(int, input().split()))

AN = sorted(AN)

for val in MN:
    start = 0
    answer = 0
    end = len(AN)-1
    while start <= end:
        mid = (start+end) // 2
        if val < AN[mid]:
            end = mid - 1
        elif val > AN[mid]:
            start = mid + 1
        if val == AN[mid]:
            answer = 1
            break
    print(answer)

