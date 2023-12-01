from itertools import permutations

M = int(input())
S = [list(map(int, input())) for _ in range(3)]

rslt = float("inf")

def return_times(i, perm):
  times = []
  
  for p in perm:
    time = []
    
    for j in range(M):
      if S[p][j] == i:
        time.append(j)
    
    if not time:
      return None
    times.append(time)
  
  return times

def return_rslt(times):
  rslt = times[0][0]
  upcnt = 0
  
  tmp = [time for time in times[1] if time > rslt%M]
  if tmp:
    rslt = tmp[0] + (upcnt * M)
  else:
    upcnt += 1
    rslt = times[1][0] + (upcnt * M)
  
  tmp = [time for time in times[2] if time > rslt%M]
  if tmp:
    rslt = tmp[0] + (upcnt * M)
  else:
    upcnt += 1
    rslt = times[2][0] + (upcnt * M)
  
  return rslt

for i in range(10):
  for perm in permutations(range(3)):
    times = return_times(i, perm)
    
    if not times: break
    
    rslt = min(rslt, return_rslt(times))

if rslt == float("inf"):
  print(-1)
else:
  print(rslt)