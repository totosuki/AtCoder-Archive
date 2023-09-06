import sys
input = sys.stdin.buffer.readline

K = int(input())
A, B = map(lambda x: int(x, K), input().split())

A,B=map(lambda x:int(x,int(input())),input().split())
print(A*B)

i=input;K=int(i());A,B=i().split();print(int(A,K)*int(B,K))

j,i=int,input;K=j(i());A,B=i().split();print(j(A,K)*j(B,K))