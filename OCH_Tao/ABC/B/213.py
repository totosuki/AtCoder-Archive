N = int(input())
A = list(map(int,input().split()))
print(A.index(sorted(A)[-2])+1)