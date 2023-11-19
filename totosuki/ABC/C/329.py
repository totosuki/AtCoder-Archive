import string

alpha = string.ascii_lowercase
N = int(input())
S = list(input())

alpha_d = dict()
for i in range(26): alpha_d[alpha[i]] = i

max = [0] * 26
now = [0] * 26

zenkai = "a"
for s in S:
  if zenkai != s:
    now[alpha_d[zenkai]] = 0
  
  now[alpha_d[s]] += 1
  if now[alpha_d[s]] > max[alpha_d[s]]:
    max[alpha_d[s]] = now[alpha_d[s]]
  zenkai = s

print(sum(max))