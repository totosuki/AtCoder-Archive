N = int(input())
R = [int(input()) for _ in range(N)]
R.sort(reverse = True)
pie = 3.14159265
rslt = 0

for i in range(N):
  if i % 2 == 0:
    rslt += R[i]**2
  else:
    rslt -= R[i]**2

rslt *= pie
print(rslt)