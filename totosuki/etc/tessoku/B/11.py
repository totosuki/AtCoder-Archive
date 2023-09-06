import sys, bisect
input = sys.stdin.buffer.readline

N = input()
A = list(map(int, input().split()))
Q = int(input())
X = [int(input()) for _ in range(Q)]
A.sort()

for x in X:
  ans = bisect.bisect_left(A, x)
  print(ans)


# コードゴルフ跡地
# import bisect;i=input;N=i();A=sorted(map(int,i().split()))
# for _ in[0]*int(i()):print(bisect.bisect_left(A,int(i())))