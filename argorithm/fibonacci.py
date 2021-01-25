def solution(n):
    arr = []
    for i in range(n+1):
        if i == 0:
            arr.append(i)
        elif i == 1:
            arr.append(i)
        else:
            arr.append(arr[i-1]+arr[i-2])
    return arr[n] % 1234567


if __name__ == '__main__':
    real_answer = solution(5)
    print(real_answer)
