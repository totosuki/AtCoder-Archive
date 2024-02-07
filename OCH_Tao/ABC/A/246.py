X1,Y1 = input().split()
X2,Y2 = input().split()
X3,Y3 = input().split()
l = []
if X1==X2:
  l.append(X3)
elif X2==X3:
  l.append(X1)
else:
  l.append(X2)
if Y1==Y2:
  l.append(Y3)
elif Y2==Y3:
  l.append(Y1)
else:
  l.append(Y2)
print(" ".join(l))