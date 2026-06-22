n = int(input())
for i in range(n):
    result = 0
    a, b, x, y = [int(j) for j in input().split()]
    if b > x:
        b -= x
        result += x
        x = 0
    else:
        x -= b
        result += b
        b = 0

    if a > y:
        a -= y
        result += y
        y = 0
    else:
        y -= a
        result += a
        a = 0
    print(result + min(a, x))