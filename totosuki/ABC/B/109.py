N = int(input())
se = set()
bf_w = ""
answer = "Yes"

for i in range(N):
  W = input()
  if i == 0:
    se.add(W)
    bf_w = W
  else:
    if (W in se) or (W[0] != bf_w[-1]):
      answer = "No"
    se.add(W)
    bf_w = W

print(answer)