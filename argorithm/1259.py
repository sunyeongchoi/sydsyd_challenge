import sys 
input = sys.stdin.readline

arr = []
while True:
    val = input().rstrip()
    if int(val) == 0:
        break
    arr.append(list(map(int, val)))

for a in arr:
    flag = 1
    if len(a)%2==0:
        while a:
            if a.pop() == a.pop(0):
                flag *= 1
            else:
                flag *= 0
    else:
        while len(a)>1:
            if a.pop() == a.pop(0):
                flag *= 1
            else:
                flag *= 0
    if flag == 1:
        print('yes')
    else:
        print('no')
    
