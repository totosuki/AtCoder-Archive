import string
S = list(input())
A = list(string.ascii_lowercase)
l = []
for i in A:
  l.append(S.count(i))
print(A[l.index(max(l))])