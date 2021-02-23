from collections import Counter
N = int(input())
N_list = input().split()
M = int(input())
M_list = input().split()

C = Counter(N_list)
print(' '.join(f'{C[m]}' if m in C else '0' for m in M_list))