A, B = map(int, input().split())
print(A + B) if int((A+B) / 24) == 0 else print((A+B) - 24)