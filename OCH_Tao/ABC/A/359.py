N = int(input())
cnt = 0
for i in [0]*N:
  S=input()
  if S[0]=="T":
    cnt+=1
print(cnt)