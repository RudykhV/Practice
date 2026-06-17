n, k = [int(i) for i in input().split()]
index = [int(i) for i in input().split()]
string = input()
result = [[index[i], string[i]] for i in range(n)]

for _ in range(k):
    for i in range(n):
        result[i][0] = index[i]
    result.sort()

print(''.join([result[i][1] for i in range(n)]))