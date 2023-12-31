S = input()
cnt = 0
for i in range(4):
  if S[i] == "+":
    cnt += 1
  else:
    cnt -= 1
print(cnt)