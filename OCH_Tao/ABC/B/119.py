N = int(input())
cnt = 0
for i in range(N):
  X,U = input().split()
  if U=="BTC":
    cnt+=float(X)*380000.0
  else:
    cnt+=float(X)
print(cnt)