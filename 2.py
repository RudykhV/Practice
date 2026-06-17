n, k = [int(i) for i in input().split()]
n += 1
arr = [[] for _ in range(n)]
for _ in range(k):
    v1, v2 = [int(i) for i in input().split()]
    arr[v1].append(v2)
    arr[v2].append(v1)

visited = [False for _ in range(n)]

def dfs(vertex):
    if visited[vertex]:
        return
    visited[vertex] = True
    for i in arr[vertex]:
        dfs(i)

result = 0
for i in range(1, n):
    if not visited[i]:
        result += 1
        dfs(i)

print(result - 1)