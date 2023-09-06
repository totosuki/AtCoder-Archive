s = input()
k = int(input())
pair_set = set()
for i in range(len(s) - k + 1):
  pair_set.add(s[i:i+k])
print(len(pair_set))