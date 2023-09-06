import sys
input = sys.stdin.buffer.readline

S = input().decode().strip()
rslt = 0

for i in range(10000):
  number = str(i).zfill(4)
  used = [False] * 10

  for n in number:
    used[int(n)] = True
  
  cnt_flag = True
  for j in range(10):
    if (S[j] == "o") and (used[j] == False): cnt_flag = False
    if (S[j] == "x") and (used[j] == True): cnt_flag = False
  
  if cnt_flag: rslt += 1

print(rslt)