# K = int(input())
# print(f"{21+K//60}:{str(K%60).zfill(2)}")
K = int(input())
print("{}:{:02}".format(21+K//60, K % 60))
