N = int(input())
A = list(map(int,input().split()))
print(sum(map(lambda x:x-10 if x>10 else 0,A)))