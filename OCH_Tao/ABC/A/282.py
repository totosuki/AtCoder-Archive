from numpy import base_repr
K = int(input())
tmp = ""
for i in range(10,K+10):
  tmp+=str(base_repr(i,36))
print(tmp)