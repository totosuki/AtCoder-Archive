N = int(input())
A = list(map(int, input().split()))
answer = "No"

for i in range(N):
  for j in range(N):
    for k in range(N):
      if i == j or j == k or k == i: continue
      if A[i] + A[j] + A[k] == 1000:
        answer = "Yes"

print(answer)