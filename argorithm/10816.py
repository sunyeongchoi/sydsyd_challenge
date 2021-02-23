N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

for ml in M_list:
    print(N_list.count(ml), end=' ')