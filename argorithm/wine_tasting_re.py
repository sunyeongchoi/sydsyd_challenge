import sys
input = sys.stdin.readline

n = int(input())
grape=[0]
for _ in range(n):
    grape.append(int(input()))
result = [0 for _ in range(n+1)]
for i in range(1,n+1):
    if i==1:
        result[1]=grape[1]
    elif i==2:
        result[2]=grape[1]+grape[2] 
    else:
        result[i]=max(result[i-3]+grape[i-1]+grape[i], result[i-2]+grape[i],result[i-1])
print(result)
print(result[-1])