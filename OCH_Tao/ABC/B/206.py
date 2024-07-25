N = int(input())
i = 0
while N>0:
  i+=1
  N-=i
print(i)

# import sympy
# from math import ceil
# N = int(input())
# X = sympy.symbols("X")
# expr = X*(X+1)/2-N
# print(max(map(lambda x:ceil(x),sympy.solve(expr,X))))