N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))


def binary(n, N, start, end):
    while start <= end:
        mid = (start+end)//2
        if n==N[mid]:
            return N[start:end+1].count(n)
        elif n<N[mid]:
            return binary(n, N, start, mid-1)
        else:
            return binary(n, N, mid+1, end)

n_dict = {}
for n in N_list:
    start=0
    end=len(N_list)-1
    if n not in n_dict:
        n_dict[n] = binary(n, N_list, start, end)

print(' '.join(str(n_dict[x]) if x in n_dict else '0' for x in M_list))