N = int(input())
l = []
for i in range(1,N):
  l.append(abs((N//i)-i)+N%i)
print(min(l) if N>1 else 0)