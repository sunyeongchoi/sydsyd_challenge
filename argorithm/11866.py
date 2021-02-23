import sys
input = sys.stdin.readline

N, K = map(int, input().split())

answer = []
arr = [i for i in range(1, N+1)]

cnt = 0
while len(arr) != len(answer):
    index = cnt%N
    print('index: ', index)
    if arr[index]==0:
        index += 1
        continue
    cnt += 1
    if (cnt % K) == 0:
        answer.append(arr[(cnt%N)-1])
        arr[(cnt%N)-1] = 0
print(answer)