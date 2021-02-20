H, M = map(int, input().split())
if H == 0:
    H = 24
sum_min = H*60+M-45
hour = sum_min//60
minute = sum_min%60
if hour==0:
    hour = 12
print(hour,minute)

