def solution(sticker):
    if len(sticker)==1:
        return sticker[0]
    arr = [0]*len(sticker)
    arr[0] = sticker[0]
    arr[1] = arr[0]
    for i in range(2, len(sticker)-1):
        arr[i] = max(arr[i-1], arr[i-2]+sticker[i])
    result = max(arr)

    arr = [0]*len(sticker)
    arr[0] = 0
    arr[1] = sticker[1]
    for i in range(2, len(sticker)):
        arr[i] = max(arr[i-1], arr[i-2]+sticker[i])
    return max(result, max(arr))

if __name__ == '__main__':
    print(solution([14,6,5,11,3,9,2,10]))