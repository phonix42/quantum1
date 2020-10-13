import numpy as np

def ReadBit(i,n):
    return (i&(1<<n))>>n

H = np.zeros((16,16))
H2 = np.zeros((16,16))
H_D = [4,0,0,0,0,-4,0,0,0,0,-4,0,0,0,0,4] #对角元：全部态一样，全为正；交替情况 全为负；其余情况正负抵消

H_Nd_1 = []
H_Nd_2 = []

for i in range(16): #第3号位子的态不一样，其他的态一样
    for j in range(16):
        if((ReadBit(i,3)!=ReadBit(j,3))and(ReadBit(i,2)==ReadBit(j,2))and(ReadBit(i,1)==ReadBit(j,1))and(ReadBit(i,0)==ReadBit(j,0))):
            H_Nd_1.append(i)
            H_Nd_2.append(j)

for i in range(16): #第2号位子的态不一样，其他的态一样
    for j in range(16):
        if((ReadBit(i,2)!=ReadBit(j,2))and(ReadBit(i,3)==ReadBit(j,3))and(ReadBit(i,1)==ReadBit(j,1))and(ReadBit(i,0)==ReadBit(j,0))):
            H_Nd_1.append(i)
            H_Nd_2.append(j)

for i in range(16): #第1号位子的态不一样，其他的态一样
    for j in range(16):
        if((ReadBit(i,1)!=ReadBit(j,1))and(ReadBit(i,2)==ReadBit(j,2))and(ReadBit(i,3)==ReadBit(j,3))and(ReadBit(i,0)==ReadBit(j,0))):
            H_Nd_1.append(i)
            H_Nd_2.append(j)
        
for i in range(16): #第0号位子的态不一样，其他的态一样
    for j in range(16):
        if((ReadBit(i,0)!=ReadBit(j,0))and(ReadBit(i,2)==ReadBit(j,2))and(ReadBit(i,1)==ReadBit(j,1))and(ReadBit(i,3)==ReadBit(j,3))):
            H_Nd_1.append(i)
            H_Nd_2.append(j)


for i in range(16): #对角元赋值
    H[i][i] = H_D[i] #g=0.5的哈密顿量
    H2[i][i] = H_D[i] #g=2的哈密顿量

for i in range(len(H_Nd_1)): #非对角元赋值
    H[H_Nd_1[i]][H_Nd_2[i]] = 0.5 #g=0.5的哈密顿量
    H2[H_Nd_1[i]][H_Nd_2[i]] = 2 #g=2的哈密顿量

H_state = np.linalg.eigvalsh(H)
H2_state = np.linalg.eigvalsh(H2)

'''
计算哈密顿量的本征能量
'''

print(H_state)
print(H2_state)