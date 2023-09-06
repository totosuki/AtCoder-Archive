import sys, itertools
input = sys.stdin.buffer.readline

def make_divisors(n):
    lower_divisors , upper_divisors = [], []
    i = 1
    while i*i <= n:
        if n % i == 0:
            lower_divisors.append(i)
            if i != n // i:
                upper_divisors.append(n//i)
        i += 1
    return lower_divisors + upper_divisors[::-1]

N, K, D = map(int, input().split())
divisors = make_divisors(D)
A = list(map(int, input().split()))
L = list()
se = set()

for a in A:
  for div in divisors[1:]:
    if a % div == 0:
      L.append(a)
      break


for combo in itertools.combinations(L, K):
  rslt = sum(combo)
  if rslt % D == 0:
    se.add(rslt)

max_num = max(se)
odds = list()

if D % 2:
  for a in A:
    if a % 2:
      odds.append(a)
  
  odds = reversed(sorted(odds))
  max_odd_num = odds[:K]
  max_num = max(max_num, sum(max_odd_num))

print(max_num) if se else print(-1)