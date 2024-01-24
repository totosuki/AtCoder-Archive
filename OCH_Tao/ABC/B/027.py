N = int(input())
A = list(map(int,input().split()))
cnt = 0
if sum(A)%N != 0:
  print(-1)
else:
  x = sum(A)//N
  l = []
  for i in range(N):
    l.append(A[i]-x)
  for i in range(N):
    if l[i]==0:
      cnt += 1
      continue
    else:
      while l[i] < 0:
        l[i] += 1
        l[i+1] -= 1
      while l[i] > 0:
        l[i] -= 1
        l[i+1] += 1
  else:
    print(N-cnt)