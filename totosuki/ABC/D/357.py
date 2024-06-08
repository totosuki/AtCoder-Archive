MOD = 998244353

N = int(input())

N_str = str(N)
d = len(N_str)
N = int(N_str)

power_10d = pow(10, d, MOD)

numerator = pow(power_10d, N, MOD) - 1
if numerator < 0:
  numerator += MOD
denominator = power_10d - 1
if denominator < 0:
  denominator += MOD

denominator_inv = pow(denominator, MOD-2, MOD)

ans = (numerator * denominator_inv) % MOD

ans = (N * ans) % MOD

print(ans)