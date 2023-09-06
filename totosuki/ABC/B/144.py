N = int(input())
answer = "No"

for i in range(1, 10):
  for j in range(1, 10):
    if i * j == N:
      answer = "Yes"

print(answer)