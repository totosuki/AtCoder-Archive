#未AC
N = int(input())
A = list(map(int,input().split()))
l = [A.index(-1)+1]
for i in range(N-1):
  x = l[i]
  l.append(A.index(x)+1)
print(" ".join(list(map(str,l))))