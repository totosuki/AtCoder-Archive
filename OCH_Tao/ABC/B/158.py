N,A,B = map(int,input().split())
print(N//(A+B)*A+min(N%(A+B),A))