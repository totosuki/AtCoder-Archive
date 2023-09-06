A, B, C, D, E, F = map(int, input().split())
diff = (A*B*C) - (D*E*F)
print(diff % 998244353)