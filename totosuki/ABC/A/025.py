import math
S = input()
N = int(input())
oneindex = math.floor(N/5) if N%5 else math.floor((N/5)-1)
twoindex = N%5-1 if N%5 else 4
print(S[oneindex] + S[twoindex])