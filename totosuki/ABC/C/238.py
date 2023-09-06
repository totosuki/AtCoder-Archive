N = int(input())
mod = 998244353
mx_digit = len(str(N))
rslt = 0

for digit in range(mx_digit):
  if digit == mx_digit-1:
    x = 10**digit
    mx = N-x+1
    rslt += (1+mx) * mx // 2
  else:
    mx = 9 * (10**digit)
    rslt += (1+mx) * mx // 2

print(int(rslt % mod))