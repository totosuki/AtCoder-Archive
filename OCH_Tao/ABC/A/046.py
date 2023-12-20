L = input().split()
x = []
for i in L:
  if i not in x:
    x.append(i)
print(len(x))