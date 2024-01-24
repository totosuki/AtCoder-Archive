N = int(input())
hh = str(N//3600).zfill(2)
N = N%3600
mm = str(N//60).zfill(2)
N = N%60
ss = str(N).zfill(2)
print(f"{hh}:{mm}:{ss}")