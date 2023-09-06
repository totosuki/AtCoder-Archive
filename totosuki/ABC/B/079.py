N = int(input())
L = [2, 1] + [0] * 85
#Make Lucas Number list
for i in range(2, len(L)):
  L[i] = L[i-1] + L[i-2]
print(L[N])