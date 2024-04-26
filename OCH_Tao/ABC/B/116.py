S = int(input())
def fn(n):
  if n%2==0:
    return n//2
  else:
    return 3*n+1
X = set()
X.add(S)
cnt = 1
tmp = S
while True:
  cnt+=1
  tmp = fn(tmp)
  if tmp not in X:
    X.add(tmp)
  else:
    print(cnt)
    break