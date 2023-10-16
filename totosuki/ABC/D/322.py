from numpy import rot90; from itertools import permutations

P1_data = [list(input()) for _ in range(4)]
P2_data = [list(input()) for _ in range(4)]
P3_data = [list(input()) for _ in range(4)]

for p1_i, p1_j in permutations(range(7), 2):
  for p2_i, p2_j in permutations(range(7), 2):
    for p3_i, p3_j in permutations(range(7), 2):
      for i in range(4):
        for j in range(4):
          for k in range(4):
            tile = [[False] * 10 for _ in range(10)]
            
            P1 = list(rot90(P1_data, k))
            P2 = list(rot90(P2_data, k))
            P3 = list(rot90(P3_data, k))

            # P1
            for i in range(4):
              for j in range(4):
                if (P1[i][j] == "#") and (not (3 <= p1_i + i <= 6 and 3 <= p1_j + j <= 6)):
                  pass
                if P1[i][j] == "#":
                  tile[i][j] = True
            
            # P2
            for i in range(4):
              for j in range(4):
                if (P2[i][j] == "#") and (not (3 <= p2_i + i <= 6 and 3 <= p2_j + j <= 6)):
                  flag = False
                if P2[i][j] == "#":
                  tile[i][j] = True

            # P3
            for i in range(4):
              for j in range(4):
                if (P3[i][j] == "#") and (not (3 <= p3_i + i <= 6 and 3 <= p3_j + j <= 6)):
                  pass
                if P2[i][j] == "#":
                  tile[i][j] = True

# print(*tile, sep = "\n")