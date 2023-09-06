N = int(input())
rslt = 0

for N in range(N):
  x, u = input().split()
  x = float(x)
  rslt += x if u == "JPY" else x * 380000

print(rslt)