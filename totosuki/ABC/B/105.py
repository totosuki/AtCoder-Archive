N = int(input())
answer = "No"

for i in range(101):
  for j in range(101):
    if 4*i + 7*j == N:
      answer = "Yes"

print(answer)