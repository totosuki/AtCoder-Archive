N = int(input())
A = [0]+list(map(int,input().split()))+[0]
D = int(input())
ll = A.copy()
lr = ll.copy()
lr.reverse()

for i in range(1,N+1):
  if ll[i] < ll[i-1]:
    ll[i] = ll[i-1]
  if lr[i] < lr[i-1]:
    lr[i] = lr[i-1]

for i in range(D):
  L,R = map(int,input().split())
  print(max(ll[ L - 1 ],lr[ N - R ]))