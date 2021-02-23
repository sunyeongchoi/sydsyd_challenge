N = int(input())
N_list = sorted(list(map(int, input().split())))
M = int(input())
M_list = list(map(int, input().split()))

for ml in M_list:
    start=0
    answer = 0
    end=len(N_list)-1
    while start <= end:
        mid = (start+end)//2
        if ml < N_list[mid]:
            end = mid-1
        elif ml > N_list[mid]:
            start = mid+1
        else:
            answer += 1
            N_list[mid] = 0
            N_list.sort()
    print(answer, end=' ')
