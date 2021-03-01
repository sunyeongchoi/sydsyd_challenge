T = int(input())
arr = [int(input()) for _ in range(T)]

def fibonacci(num):
    zero_cnt = [1, 0]
    one_cnt = [0, 1]
    if num <= 1:
        return
    
    for i in range(2, num+1):
        zero_cnt.append(zero_cnt[i-1] + zero_cnt[i-2])
        one_cnt.append(one_cnt[i-1] + one_cnt[i-2])
    return zero_cnt, one_cnt

zero_cnt, one_cnt = fibonacci(40)

for a in arr:
    print(zero_cnt[a], one_cnt[a])
