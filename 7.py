from re import fullmatch

if fullmatch(r"\D\d\d\d\D\D", input()):
    print("YES")
else:
    print("NO")