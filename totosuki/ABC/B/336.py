N = int(input())
x = bin(N)
answer = 0

for i in range(1, 1000):
  if x[-i] == "0":
    answer += 1
  else:
    break

print(answer)