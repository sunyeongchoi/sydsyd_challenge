def solution(n, computers):
    visited = [False for _ in range(n)]
    answer = 0
    
    for com in range(n):
        if not visited[com]:
            dfs(n, computers, com, visited)
            answer +=1 
    return answer

def dfs(n, computers, com, visited):
    visited[com] = True
    for connect in range(n):
        if connect!=com and computers[com][connect]==1 and not visited[connect]:
            dfs(n, computers, connect, visited)

if __name__ == '__main__':
    real_answer = solution(3, [[1, 1, 0], [1, 1, 0], [0, 0, 1]])
    print(real_answer)