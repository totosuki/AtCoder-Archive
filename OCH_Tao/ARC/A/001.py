N = int(input())
C = list(map(int,list(input())))
L = [0]*4
for i in C:
  L[i-1]+=1
print(f"{max(L)} {min(L)}")