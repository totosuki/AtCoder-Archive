from string import ascii_lowercase

S = input()
d = dict()

for t in ascii_lowercase:
    d[t] = S.count(t)

mx = max(d.values())
ans = ""

for s in S:
    if d[s] != mx:
        ans += s

print(ans)
