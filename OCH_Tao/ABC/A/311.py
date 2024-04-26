N = int(input())
S = input()
D = {"A":0,"B":0,"C":0}
for i in range(N):
  D[S[i]]=D[S[i]]+1
  if min(D.values())>0:
    print(i+1)
    break