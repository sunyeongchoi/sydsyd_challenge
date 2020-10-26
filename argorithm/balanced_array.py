def balanced_sum(arr):
    size = arr.pop(0)
    for i in range(size):
        # print('arr[:i+1]: ', arr[:i+1])
        # print('arr[-(len(arr)-i):]: ', arr[-(len(arr)-i):])
        if sum(arr[:i+1]) == sum(arr[-(len(arr)-i):]):
            return i


if __name__ == '__main__':
    real_answer = balanced_sum([4, 1, 2, 3, 3])
    print(real_answer)
