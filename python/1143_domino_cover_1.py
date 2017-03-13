'''
斐波拉切数列的快速计算，指数级计算
'''
n = int(raw_input())

m = [[0, 1], [1, 1]]

def mat(m1, m2):
    m3 = [[0, 0],[0, 0]]
    for i in xrange(2):
        for j in xrange(2):
            m3[i][j] = m1[i][0]*m2[j][0] + m1[i][1]*m2[j][1]
            # 防止溢出
            m3[i][j] = m3[i][j] % 19999997
    return m3

bit_n = []
while n > 0:
    bit_n.append(n%2)
    n = n / 2

M = [[1,0],[0,1]]
for i in bit_n:
    if i == 1:
        M = mat(M, m)
    m = mat(m, m)

print M[1][1] % 19999997
