h, w = [int(i) for i in input().split()]
arr = [[int(i) for i in input().split()] for _ in range(h)]
min_x, max_x, min_y, max_y = 100, 0, 100, 0

for i in range(h):
    for j in range(w):
        if arr[i][j] == 1:
            min_x = min(min_x, j)
            max_x = max(max_x, j)
            min_y = min(min_y, i)
            max_y = max(max_y, i)

print(min_x - 1, min_y - 1, max_x + 1, max_y + 1)
