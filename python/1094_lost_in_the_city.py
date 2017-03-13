n, m = [int(x) for x in raw_input().split()]

city = []
for i in xrange(n):
    city.append([x for x in raw_input()])

surround = []
for i in xrange(3):
    surround.append([x for x in raw_input()])

def isMatch(city, p1, p2, surround):
    index = [[0,0],[0,1],[0,2],[1,2],[2,2],[2,1],[2,0],[1,0]]
    for i in [0,2,4,6]:
        p = 0
        flag = True
        while p < 8 and flag:
            i = i % 8
            c1, c2 = p1+index[i][0]-1, p2+index[i][1]-1
            s1, s2 = index[p][0], index[p][1]
            if city[c1][c2] != surround[s1][s2]:
                flag = False
            p += 1
            i += 1
        if flag:
            return True
    return False

for i in xrange(1, n-1):
    for j in xrange(1, m-1):
        if city[i][j] == surround[1][1]:
            if isMatch(city, i, j, surround):
                print i+1, j+1
