from math import sqrt
N = int(input())
X = list(map(int,input().split()))
print(sum(map(abs,X)))
print(sqrt(sum(map(lambda x:abs(x**2),X))))
print(max(map(abs,X)))