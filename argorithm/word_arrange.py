import sys
input = sys.stdin.readline

# 입력
N = int(input().rstrip())
arr = set(input().rstrip() for _ in range(N)) # 중복 제거

# 길이가 짧은 것부터, 길이가 같으면 사전 순으로
answer = sorted(sorted(arr), key=lambda x: len(x))

# 출력
[print(a) for a in answer]
