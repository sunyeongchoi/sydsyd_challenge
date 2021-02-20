arr = [input() for _ in range(3)]
A, B, C = arr

result = list(map(int, str(int(A)*int(B)*int(C))))

for i in range(10):
    print(result.count(i))