T = int(input())
for i in range(T):
  N = int(input())
  A = list(map(int,input().split()))
  print(len([i for i in A if i%2==1]))