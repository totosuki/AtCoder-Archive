from collections import defaultdict

[print(l[2])for l in sorted([[S,-int(P),i+1]for i in range(int(input()))for S,P in [input().split()]])]

d=[]
for i in range(int(input())):
  S,P=input().split()
  d.append([S,-int(P),i+1])
[print(l[2]) for l in sorted(d)]

# P = [] 
# dict = defaultdict(list)
# for _ in range(N):
#   s, p = input().split()
#   p = int(p)
#   P.append(p)
#   dict[s].append(p)

# dict = sorted(dict.items())

# for k, d in dict:
#   d.sort(reverse = True)
#   for i in range(len(d)):
#     print(P.index(d[i]) + 1)