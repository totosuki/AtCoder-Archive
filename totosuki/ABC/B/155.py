N = int(input())
A = list(map(int, input().split()))
answer = "APPROVED"

for i in range(N):
  if A[i] % 2 == 0:
    if A[i] % 3 != 0 and A[i] % 5 != 0:
      answer = "DENIED"

print(answer)