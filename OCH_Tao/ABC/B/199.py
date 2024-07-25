N = int(input())
A = list(map(int,input().split()))
B = list(map(int,input().split()))
print(max(min(B)-max(A)+1,0))