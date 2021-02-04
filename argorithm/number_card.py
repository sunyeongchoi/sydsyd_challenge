import sys
input = sys.stdin.readline

N = int(input())
N_arr = sorted(list(map(int, input().split())))
M = int(input())
M_arr = list(map(int, input().split()))

for marr in M_arr:
    answer = 0
    start = 0
    end = len(N_arr) - 1
    while start <= end:
        mid = (start + end) // 2
        if N_arr[mid] > marr:
            end = mid-1
        elif N_arr[mid] < marr:
            start = mid+1
        else:
            answer = 1
            break
    print(answer, end=' ')
