N=int(input())
A=list(map(int,input().split()))
print(*[i for i in A if i%2==0])