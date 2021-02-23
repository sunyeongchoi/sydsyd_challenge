T = int(input())
for i in range(T):
    H, W, N = map(int, input().split())
    cnt = 0
    for i in range(W):
        for j in range(H):
            cnt += 1
            if cnt == N:
                if i+1 > 9:
                    print(str(j+1)+str(i+1))
                    break
                else:
                    print(str(j+1)+'0'+str(i+1))
                    break

