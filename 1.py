from copy import deepcopy

n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

result = deepcopy(arr)

for i in range(1, n):
    for j in range(i + 1):
        if j == 0:
            result[i][j] += result[i - 1][0]
        elif i == j:
            result[i][j] += result[i - 1][i - 1]
        else:
            result[i][j] += min(result[i - 1][j - 1], result[i - 1][j])

min_sum = min(result[n - 1])

index = result[n - 1].index(min_sum)
s = [arr[n - 1][index]]

for i in range(n - 1, 0, -1):
    if index == 0:
        for j in range(i - 1, -1, -1):
            s.append(arr[j][0])
        break
    if index == i:
        for j in range(i - 1, -1, -1):
            s.append(arr[j][j])
        break
    if result[i - 1][index - 1] > result[i - 1][index]:
        s.append(arr[i - 1][index])
    else:
        s.append(arr[i - 1][index - 1])
        index -= 1

print(min_sum)
print(*reversed(s))


