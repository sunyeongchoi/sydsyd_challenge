N = int(input())
people = [tuple(map(int, input().split())) for _ in range(N)]

for c in people:  # 입력 값
    rank = 1  # 랭킹 기본 값은 1로 세팅

    for n in people: # 입력 값과 입력 값을 비교하기 위해 for 문으로 또 people을 돌린다.
        if (c[0] != n[0]) & (c[1] != n[1]):  # 자기 자신과 비교하면 안되기 때문에
            if (c[0] < n[0]) & (c[1] < n[1]):  # 키, 몸무게 둘다 큰 사람 발견시 자신의 랭크 + 1
                rank += 1
    print(rank, end=' ')
