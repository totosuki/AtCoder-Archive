import sys
input = sys.stdin.buffer.readline

S1, S2, S3 = [input().decode() for _ in range(3)]
T = input().decode()
rslt = str()

for t in T:
  if t == "1":
    rslt += S1
  elif t == "2":
    rslt += S2
  elif t == "3":
    rslt += S3

print(rslt.replace("\n", ""))