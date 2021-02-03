# n 입력받기
n = int(input())

# 단어 입력받을 리스트 만들기
words = []

# 단어 입력받기
for i in range(n):
  words.append(input())
# 딕셔너리 초기화하기
dict = {}
# 딕셔너리에 알파벳당 숫자 집어넣기
for word in words:
  k = len(word)-1
  for s in word:
    if s in dict:
      dict[s] += pow(10, k)
    else:
      dict[s] = pow(10, k)
    k -= 1

# 숫자 리스트 초기화하기
nums = []
# 사전의 값들만으로 이루어진 리스트 초기화하기
for value in dict.values():
  nums.append(value)

# 숫자 큰순으로 정렬하기
nums.sort(reverse=True)

# 출력할 값과 곱해야하는 수 초기화하기
result, t = 0, 9

# 값 구하기
for i in range(len(nums)):
  result += nums[i]*t
  t -= 1

print(result)
