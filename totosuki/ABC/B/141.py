S = input()
answer = "Yes"

for i, s in enumerate(S):
  i += 1
  if (i % 2 == 1 and s == "L") or (i % 2 == 0 and s == "R"):
    answer = "No"

print(answer)