N = int(input())
H = list(map(int,input().split()))
T = 0
for i in H:
  T+=i//5*3
  M = i%5
  while M>0:
    if T%3==2:
      T+=1
      M-=3
    else:
      T+=1
      M-=1
print(T)