from collections import defaultdict

N = int(input())
dict = defaultdict(int)
for _ in range(N):
  s = input()
  dict[s] += 1

max_i = max(dict.values())
rslt = [k for k, i in dict.items() if i == max_i]
print(rslt[0])