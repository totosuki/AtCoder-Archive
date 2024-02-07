K,S = map(int,input().split())
cnt = 0
for x in range(K+1):
  if x>S:
     break
  for y in range(K+1):
    if x+y > S:
       break
    else:
      if 0 <= S-x-y <= K:
        cnt += 1
print(cnt)