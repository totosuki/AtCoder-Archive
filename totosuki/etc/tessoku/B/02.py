A, B = map(int, input().split())
answer = "No"

for n in range(A, B+1):
  if 100 % n == 0:
    answer = "Yes"

print(answer)