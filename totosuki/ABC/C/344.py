N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))
L = int(input())
C = list(map(int, input().split()))
Q = int(input())
X = list(map(int, input().split()))

can = {a + b + c for a in A for b in B for c in C}

for x in X:print("NYoe s"[x in can::2])