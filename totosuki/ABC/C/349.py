S = list(input())
T = list(input())

t_cnt = 0
ans = "No"

for i in range(len(S)):
  if S[i] == T[t_cnt].lower():
    t_cnt += 1

  if t_cnt == 3:
    ans = "Yes"
    break
else:
  if t_cnt == 2 and T[2] == "X":
    ans = "Yes"

print(ans)
