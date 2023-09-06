A, B, C = map(int, input().split())
rslt = A * B * 2
rslt += B * C * 2
rslt += A * C * 2
print(rslt)