import heapq

def solution(scoville, K):
    heap = []
    for num in scoville:
        heapq.heappush(heap, num)
    
    answer = 0
    while heap[0] < K:
        answer += 1
        try:
            heapq.heappush(heap, heapq.heappop(heap)+(heapq.heappop(heap)*2))
        except IndexError:
            return -1
    return answer

if __name__ == '__main__':
    real_answer = solution([1, 2, 3, 9, 10, 12], 7)
    print(real_answer)