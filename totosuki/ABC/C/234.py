K = int(input())
K_b = bin(K)[2:]
rslt = []

for k in K_b:
  rslt.append(int(k)*2)

print(*rslt, sep = "")