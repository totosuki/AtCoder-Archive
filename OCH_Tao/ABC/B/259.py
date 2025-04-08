import numpy as np
a,b,d = map(int,input().split())
D = np.radians(d)
print(*np.dot(np.array([[np.cos(D),-np.sin(D)],[np.sin(D),np.cos(D)]]),np.array([a,b])))