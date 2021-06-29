# dfs 풀이
def solution(n, computers):
    answer = 0
    visited = [True for i in range(n)]
    for i in range(n):
        if visited[i]:
            dfs(i, n, visited, computers)
            answer += 1
    return answer

def dfs(i, n, visited, computers):
    visited[i] = False
    for j in range(n):
        if i == j:
            continue
        if visited[j] and computers[i][j] == 1:
            dfs(j, n, visited, computers)



# bfs 풀이
from collections import deque
def solution(n, computers):
    answer = 0
    visited = [True for i in range(n)]
    for i in range(n):
        if visited[i]:
            bfs(i, n, visited, computers)
            answer += 1
    return answer

def bfs(i, n, visited, computers):
    queue = deque([])
    queue.append(i)
    while queue:
        i = queue.popleft()
        visited[i] = False
        for j in range(n):
            if i == j:
                continue
            if visited[j] and computers[i][j] == 1:
                queue.append(j)
