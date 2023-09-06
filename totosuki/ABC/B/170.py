X, Y = map(int, input().split())
answer = "No"

for i in range(X+1):
  tmp = (i * 2) + ((X-i) * 4)
  if tmp == Y:
    answer = "Yes"

print(answer)