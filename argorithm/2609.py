A, B = map(int, input().split())
min_num = min(A, B)
max_num = max(A, B)

# 최대 공약수
for i in range(min_num, 0, -1):
    if min_num%i==0 and max_num%i==0:
        print(i)
        break

# 최소 공배수
increase = 1
while True:
    result = min_num*increase
    if (result)%max_num==0:
        print(result)
        break
    else:
        increase+=1
