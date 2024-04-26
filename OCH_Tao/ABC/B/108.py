X1,Y1,X2,Y2 = map(int,input().split())
inc = [X2-X1,Y2-Y1]
rslt = []
rslt.append(X2-inc[1])
rslt.append(Y2+inc[0])
rslt.append(rslt[0]-inc[0])
rslt.append(rslt[1]-inc[1])
print(" ".join([str(i) for i in rslt]))