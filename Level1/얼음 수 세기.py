def dfs(x, y):
    if x>n-1 or x<0 or y>m-1 or y<0:
        return False

    if graph[x][y] == 0:
        graph[x][y] =1
        dfs(x-1,y)
        dfs(x, y-1)
        dfs(x+1,y)
        dfs(x, y+1)
        return True
    return False


n, m = map(int, input().split())
graph = []
ans = 0
for i in range(n):
    graph.append(list(map(int, input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            dfs(i, j)
            ans += 1

print(ans)
