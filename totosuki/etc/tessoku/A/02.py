N, X = map(int, input().split())
A = list(map(int, input().split()))
answer = "No"

for a in A:
  if a == X:
    answer = "Yes"

print(answer)