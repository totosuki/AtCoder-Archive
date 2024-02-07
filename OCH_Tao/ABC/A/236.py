S = input()
A,B = map(int,input().split())
print(S[:A-1]+S[B-1]+S[A:B-1]+S[A-1]+S[B:])