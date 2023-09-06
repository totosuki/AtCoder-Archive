_=input()
[print(s+t,end="")for S,T in input().split() for s,t in zip(S,T)]

# S, T = input().split()
# for s, t in zip(S, T):
#   print(s + t, end = "")