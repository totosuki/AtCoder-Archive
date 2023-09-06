N = int(input())
A = list(map(int,input().split()))
for i in range(min(A),max(A)):
    if not i in A:
        print(i)