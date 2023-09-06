def binary_search_start(x, y):
  min = 0
  max = len(x)-1
  while min <= max:
    middle = (min+max) // 2
    if x[middle-1] <= y <= x[middle]:
      return middle
    elif x[middle] < y:
      min = middle + 1
    else:
      max = middle - 1
  return middle

def binary_search_end(x, y):
  min = 0
  max = len(x)-1
  while min <= max:
    middle = (min+max) // 2
    if x[middle - 1] <= y <= x[middle]:
      return middle
    elif x[middle] < y:
      min = middle + 1
    else:
      max = middle - 1
  return middle

def convert_1d_to_2d(l, cols):
  return [l[i:i + cols] for i in range(0, len(l), cols)]

N = int(input())
A = list(map(int, input().split()))
clean_A = convert_1d_to_2d(A[1:], 2)
Q = int(input())
all_data = [list(map(int, input().split())) for _ in range(Q)]
for data in all_data:
  start = binary_search_start(A, data[0])
  end = binary_search_end(A, data[1])
  clean_A = clean_A[start//2-1:end//2]
  print(f"data: {data} |||| {clean_A}")
  rslt = 0
  for d in clean_A:
    rslt += d[1] - d[0]
  if start % 2 == 0:
    rslt -= data[0] - clean_A[0][0]
  if end % 2 == 0:
    rslt -= clean_A[-1][1] - data[1]
  if start % 2 == 1:
    if start == clean_A[0][1]:
      print("aa")
      rslt -= clean_A[0][1] - clean_A[0][0]
  print(rslt)





