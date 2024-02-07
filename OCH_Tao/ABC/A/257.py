from math import ceil
N,X = map(int,input().split())
print(chr(ceil(X/N)+64))