import sys, string
input = sys.stdin.buffer.readline

P = list(map(int, input().split()))
alphabet = string.ascii_lowercase
rslt = list()

for p in P:
  rslt.append(alphabet[p-1])

print("".join(rslt))