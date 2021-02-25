from collections import deque

def solution(priorities, location):
    answer, i = 0, 0
    queue = deque()
    for p in priorities:
        queue.append((i, p))
        i+=1

    while queue:
        cur = queue.popleft()
        if any(cur[1] < q[1] for q in queue):
            queue.append((cur))
        else:
            answer += 1
            if cur[0] == location:
                return answer

if __name__ == '__main__':
    real_answer = solution([2, 1, 3, 2], 1)
    print(real_answer)