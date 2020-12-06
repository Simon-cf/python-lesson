X = [[12, 7, 3],
     [4, 5, 6],
     [7, 8, 9]]

Y = [[5, 8, 1],
     [6, 7, 3],
     [4, 5, 9]]
Z = []
for i in range(len(X)):
     Z_ = []
     for k in range(len(Y)):
          Z_.append(X[i][k] + Y[i][k])
     else:
          Z.append(Z_)
for m in Z:
     print(m)
