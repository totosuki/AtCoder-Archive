N = int(input())
rslt = []

i = 1
while i*i <= N:
  diff = abs(i - (N//i))
  amari = N % i
  rslt.append(diff + amari)
  i += 1

print(min(rslt))