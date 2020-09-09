def solution(scoville, K):
    answer = 0
    scoville.sort()
    smallest_num = scoville[0]
    while smallest_num < K:
        first = scoville.pop(0)
        second = scoville.pop(0)
        mixed_scovile_num = first + (second*2)
        answer += 1
        scoville.append(mixed_scovile_num)
        scoville.sort()
        smallest_num = scoville[0]
    return answer


if __name__ == '__main__':
    real_answer = solution([1, 2, 3, 9, 10, 12], 7)
    print(real_answer)