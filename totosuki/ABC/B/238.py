(i:=input)()
A,L,m=map(int,i().split()),[1]+[0]*359,{0}
r=c=0
for a in A:r,L[r]=(r+a)%360,1
print(max((c:=c*(-l+1)+1)for l in L))

# _,A,L,m=input(),map(int,input().split()),[1]+[0]*359,{0}
# r=c=0
# for a in A:r,L[r]=(r+a)%360,1
# print(max([(c:=1)if l else(c:=c+1)for l in L]))

# import sys
# input = sys.stdin.buffer.readline

# N = int(input())
# A = list(map(int, input().split()))
# angle = 0
# L = [False] * 360
# L[0] = True
# rslt = list()

# for a in A:
#   angle += a
#   angle %= 360
#   L[angle] = True

# cnt = 0
# for i in range(360):
#   cnt += 1
#   if L[i] == True:
#     rslt.append(cnt)
#     cnt = 0
# else:
#   cnt += 1
#   rslt.append(cnt)

# print(max(rslt)
