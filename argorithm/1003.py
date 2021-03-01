T = int(input())
arr = [int(input()) for _ in range(T)]
def fibonacci(num):
    global zero
    global one
    if num==0:
        zero += 1
        return 0
    elif num==1:
        one += 1
        return 1
    else:
        return fibonacci(num-1)+fibonacci(num-2)
for a in arr:
    zero = 0
    one = 0
    result = fibonacci(a)
    print(zero, one)