from collections import*
D=defaultdict(int)
exec("D[input()]+=1;"*int(input()))
print(sorted(D.items(),key=lambda x:-x[1])[0][0])