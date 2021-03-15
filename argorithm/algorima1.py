from collections import deque

def bfs(board, i, j, visited):
    dx, dy = [-1, 1, 0, 0], [0, 0, -1, 1]
    val = board[i][j]
    queue = deque([(i, j, 1)])
    while queue:
        x, y, cnt = queue.popleft()
        for k in range(4):
            nx, ny = x+dx[k], y+dy[k]
            if not(0<=nx<4 and 0<=ny<4):
                continue
            if board[nx][ny]==val and visited[x][y]<2:
                visited[x][y]+=1
                queue.append((nx, ny, cnt+1))
    return cnt

def solution(board):
    visited = [[0]*4 for _ in range(4)]
    answer = []
    for i in range(4):
        for j in range(4):
            answer.append(bfs(board, i, j, visited))
    if max(answer) > 1:
        return max(answer)
    else:
        return -1

if __name__ == '__main__':
    print(solution([[3,2,3,2],[2,1,1,2],[1,1,2,1],[4,1,1,1]]))
