def solution(scoville, K):
    answer = 0
    while min(scoville) < K:
        answer += 1
        scoville.append(scoville.pop(0) + (scoville.pop(0)*2))
        scoville.sort()
    return answer


if __name__ == '__main__':
    real_answer = solution([1, 2, 3, 9, 10, 12], 7)
    print(real_answer)