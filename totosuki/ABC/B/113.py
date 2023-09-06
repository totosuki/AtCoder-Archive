N = int(input())
T, A = map(int, input().split())
H = list(map(int, input().split()))
H_abs = []
for h in H:
  tmp = T - (h * 0.006)
  H_abs.append(abs(A - tmp))
print(H_abs.index(min(H_abs)) + 1)