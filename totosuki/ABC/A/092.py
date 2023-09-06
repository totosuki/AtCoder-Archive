A = int(input())
B = int(input())
C = int(input())
D = int(input())
rslt = 0
if A > B:
  rslt += B
else:
  rslt += A

if C > D:
  rslt += D
else:
  rslt += C

print(rslt)