N, K = map(int, input().split())
if N-K > 0:
    M = N-K
else:
    M = 1

C_N = 1
for i in range(1, N+1):
    C_N*=i

C_M = 1
for j in range(1, M+1):
    C_M*=j

C_K = 1
for a in range(1, K+1):
    C_K*=a

print(int(C_N/(C_M*C_K)))