n, k = [int(i) for i in input().split()]
n += 1
arr = [0 for _ in range(n)]
for _ in range(k):
    command, input1, input2 = [int(i) for i in input().split()]
    if command == 1:
        arr[input1] += input2
    else:
        print(sum(arr[input1:input2 + 1]))