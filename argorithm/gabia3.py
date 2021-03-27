def solution(N, coffee_times):
    answer, making, coffee_times_tupple = [], [], []
    for index, coffee_time in enumerate(coffee_times):
        coffee_times_tupple.append((index+1, coffee_time))
    
    while True:
        while True:
            if len(making) < N and coffee_times_tupple:
                making.append(coffee_times_tupple.pop(0))
            elif len(making) == N:
                break
            elif len(coffee_times_tupple) < N:
                break

        temp = []
        min_value = min(making, key=lambda x: x[1])[1]
        for m in range(len(making)):
            index, value = making[m]

            if value == min_value: 
                answer.append(index)
                temp.append(m)

        while temp:
            index = temp.pop()
            making.pop(index)

        for i, m2 in enumerate(making):
            index, value = m2
            making[i] = (index, value-min_value)         

        print('making : ', making)
        if not making:
            return answer
    return answer

if __name__ == '__main__':
    print(solution(1, [100, 1, 50, 1, 1]))