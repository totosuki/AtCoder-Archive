S = input()
answer = "Yes"

for i in range(1, 16, 2):
  if S[i] == "1":
    answer = "No"

print(answer)