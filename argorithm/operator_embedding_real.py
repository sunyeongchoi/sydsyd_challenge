from itertools import permutations

# 입력값 3줄
N = int(input())
A = list(map(int, input().split()))
add, sub, multi, div = map(int, input().split())
# 연산자 입력 받은 것을 N-1개의 배열로 각각의 연산자의 갯수에 맞춰 넣어준다.
operation = []
operation += ['+']*add
operation += ['-']*sub
operation += ['*']*multi
operation += ['/']*div
# permutations 라는 것을 통해 연산자의 모든 경우의 수를 구한다(순열 -> 순서 상관 있음), set을 통해 중복 값 제거
operation_list = list(set(permutations(operation)))
# 결과가 항상 -10억 ~ 10억 이라고 했기 때문에, 추후에 결과와 비교할 MAX와 MIN의 초깃값을 다음과 같이 주었다.
MAX = -10e9-1
MIN = 10e9+1
# 순열이 담긴 operation_list에서 하나씩 빼서 해당 경우의 수를 다 계산해준다.
# operation_list는 [('+', '-', '*', '/', '+'), ('+', '-', '/', '*', '+'),...] 이와 같이 나온다.
# 각각 튜플에 N-1개의 연산자가 담겨있기 때문에 이를 다 계산한뒤, 최댓값 최솟값을 리턴한다.
print(operation_list)
for o in operation_list:
    answer = A[0]
    for i in range(N-1):
        if o[i] == '+':
            answer += A[i+1]
        elif o[i] == '-':
            answer -= A[i+1]
        elif o[i] == '*':
            answer *= A[i+1]
        else:
            if answer < 0:
                answer = -(-answer//A[i+1])
            else:
                answer //= A[i+1]

    if answer < MIN:
        MIN = answer
    if answer > MAX:
        MAX = answer

print(MAX)
print(MIN)
