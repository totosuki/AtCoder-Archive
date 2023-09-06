import sys, itertools 
input = sys.stdin.buffer.readline 
N = int(input()) 
alpha = ["a","b","c"] 
perm = list(itertools.product(alpha, repeat = N)) 
[print("".join(p)) for p in perm] 