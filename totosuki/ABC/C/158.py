from time import perf_counter

st = perf_counter()
nt = perf_counter()

A, B = map(int, input().split())
rslt = 0
answer = -1

while nt - st < 1.9:
  rslt += 1
  if rslt * 0.08 // 1 == A and rslt * 0.1 // 1 == B:
    answer = rslt
    break
  
  nt = perf_counter()

print(answer)