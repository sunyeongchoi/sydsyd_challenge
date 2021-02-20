N = int(input())
arr = list(map(int, input().split()))

answer = 0
for a in arr:
    cnt = 0
    if a == 1:
        continue
    for b in range(2, a):
        if a%b==0: 
            cnt+=1
    if cnt == 0:
        answer += 1
print(answer)