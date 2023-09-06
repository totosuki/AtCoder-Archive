N, Q = map(int, input().split())
events = [list(map(int, input().split())) for _ in range(Q)]
statuses = [0 for _ in range(N)]
for i in range(len(events)):
  event = events[i]
  if event[0] == 1:
    statuses[event[1]-1] += 1
  elif event[0] == 2:
    statuses[event[1]-1] += 2
  else:
    if statuses[event[1]-1] >= 2:
      print("Yes")
    else:
      print("No")