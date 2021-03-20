def solution(table, languages, preference):
    answer = []
    for t in table:
        num = 6
        table_list = t.split()
        sum = 0
        for tl in table_list:
            for lp, val in list(zip(languages,preference)):
                if tl == lp:
                    sum += (int(val)*int(num))
            num -= 1
        answer.append(sum)
    index = list(filter(lambda x: answer[x] == max(answer), range(len(answer))))
    final_answer = []
    for i in index:
        final_answer.append(table[i].split()[0])
    return sorted(final_answer)[0]

if __name__ == '__main__':
    print(solution(["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["PYTHON", "C++", "SQL"], [7, 5, 5]))
    # print(solution(	["SI JAVA JAVASCRIPT SQL PYTHON C#", "CONTENTS JAVASCRIPT JAVA PYTHON SQL C++", "HARDWARE C C++ PYTHON JAVA JAVASCRIPT", "PORTAL JAVA JAVASCRIPT PYTHON KOTLIN PHP", "GAME C++ C# JAVASCRIPT C JAVA"], ["JAVA", "JAVASCRIPT"], [7, 5]))