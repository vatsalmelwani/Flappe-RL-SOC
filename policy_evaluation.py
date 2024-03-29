import numpy as np
v=np.zeros((4,4))
V=np.zeros((4,4))
for k in range(3):
    for i in range(4):
        for j in range(4):
            if 0<i<3 and 0<j<3:
                V[i][j]=((v[i+1][j]+v[i-1][j]+v[i][j+1]+v[i][j-1])/4)-1
            if 0<i<3 and j==0:
                V[i][j]=((v[i+1][j]+v[i-1][j]+v[i][j+1])/3)-1
            if 0<i<3 and j==3:
                V[i][j]=((v[i+1][j]+v[i-1][j]+v[i][j-1])/3)-1
            if i==0 and 0<j<3:
                V[i][j]=((v[i+1][j]+v[i][j+1]+v[i][j-1])/3)-1
            if i==3 and 0<j<3:
                V[i][j]=((v[i-1][j]+v[i][j+1]+v[i][j-1])/3)-1
            if i==0 and j==0:
                V[i][j]=0
            if i==3 and j==3:
                V[i][j]=0
            if i==0 and j==3:
                V[i][j]=((v[i+1][j]+v[i][j-1])/2)-1
            if i==3 and j==0:
                V[i][j]=((v[i-1][j]+v[i][j+1])/2)-1
            #print(V)
    v=V
    V=np.zeros((4,4))
    #print(v)
print(v)
