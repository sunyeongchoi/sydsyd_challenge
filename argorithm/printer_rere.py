from collections import deque

def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    final_loc = []

    while priorities:
        if priorities[0] == max(priorities):
            final_loc.append(loc.pop(0))
            priorities.pop(0)
        else:
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
    
    print(final_loc)
    return final_loc.index(location)+1

if __name__ == '__main__':
    real_answer = solution([1, 1, 9, 1, 1, 1], 0)
    print(real_answer)