import math
data = [input() for _ in range(5)]
rslt = 0
cnt = 0

for i in range(5):
  if data[i][-1] == "0":
    cnt += 1
    rslt += int(data[i])

for i in reversed(range(1, 10)):
  for j in range(5):
    if data[j][-1] == str(i):
      cnt += 1
      if cnt == 5:
        rslt += int(data[j])
      else:
        rslt += int(math.ceil(int(data[j]) / 10) * 10)

print(rslt)