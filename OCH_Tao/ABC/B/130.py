N,X = map(int,input().split())
L = list(map(int,input().split()))
tmp = [0]
for i in L:
  tmp.append(tmp[-1]+i)
print(len([i for i in tmp if i<=X]))