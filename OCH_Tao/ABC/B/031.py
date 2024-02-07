L,H = map(int,input().split())
N = int(input())
for i in range(N):
  a = int(input())
  if L<=a<=H:
    print(0)
  elif a>H:
    print(-1)
  else:
    print(L-a)