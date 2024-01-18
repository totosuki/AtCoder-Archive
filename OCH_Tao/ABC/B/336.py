N = int(input())
x = bin(N)
cnt = 0
for i in range(-1,-len(x),-1):
  if x[i] != "1":
    cnt += 1
  else:
    break
print(cnt)