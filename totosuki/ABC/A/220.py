A, B, C = map(int, input().split())
for n in range(A, B+1):
  if n % C == 0:
    print(n)
    exit()
print(-1)