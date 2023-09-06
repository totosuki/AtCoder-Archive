S = list(map(int, input().split()))
sort_s = sorted(S)
answer = "Yes"

if S != sort_s:
  answer = "No"

for s in S:
  if not (100 <= s <= 675):
    answer = "No"
  if s % 25 != 0:
    answer = "No"

print(answer)