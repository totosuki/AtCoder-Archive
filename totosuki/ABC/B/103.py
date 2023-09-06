S = input()
T = input()
answer = "No"

for i in range(len(S)):
  S = S[-1] + S[0:-1]
  if S == T:
    answer = "Yes"

print(answer)