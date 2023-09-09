from fractions import Fraction
N = int(input())
print(eval(str(Fraction(1,sum(map(lambda x: Fraction(1, x), list(map(int, input().split()))))))))

print(1/sum(1/int(a)for a in[*open(0)][1].split()))

# N = int(input())
# A = list(map(int, input().split()))
# sm = 0
# for a in A:
#   sm += 1 / a
# print(1 / sm)