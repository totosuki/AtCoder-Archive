import collections
N = int(input())
R = list(input())
C = collections.Counter(R)
cnt = 0
cnt += C.get("A",0)*4
cnt += C.get("B",0)*3
cnt += C.get("C",0)*2
cnt += C.get("D",0)*1
print(cnt/N)