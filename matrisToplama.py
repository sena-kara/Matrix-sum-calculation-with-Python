# # -*- coding: utf-8 -*-
# # matris
# 1 3 5
# 2 4 1
# 1 5 7

# 3 3 4
# 2 4 1
# 3 5 4

# 4 6 9
# 4 8 2
# 4 10 11

x = [[1,3,5],[2,4,1],[1,5,7]]
y = [[3,3,4],[2,4,1],[3,5,4]]

sonuc= [[0,0,0],[0,0,0],[0,0,0]]

sonuc[0][0]= x[0][0]+y[0][0]
print(sonuc)

for i in range(len(x)):
    for j in range(len(y)):
        sonuc[i][j]= x[i][j]+y[i][j]
print(sonuc)

                                