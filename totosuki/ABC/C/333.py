N = int(input())

repu_list = []
for i in range(1, 20):
  repunit = int("1"*i)
  repu_list.append(repunit)

repu = []

for i in range(len(repu_list)):
  for j in range(len(repu_list)):
    for k in range(len(repu_list)):
      repu.append(repu_list[i]+repu_list[j]+repu_list[k])

repu = sorted(set(repu))

print(repu[N-1])