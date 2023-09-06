K = int(input())
A, B = map(int, input().split())
for n in range(A, B+1):
  if n % K == 0:
    print("OK")
    exit()
print("NG")