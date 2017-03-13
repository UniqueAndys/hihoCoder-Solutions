n = input()

import sys
import copy

def dele(p):
    flag = True
    while flag:
        q = []
        i = 0
        index = 0
        while i < len(p):
            if p[i] != p[index]:
                if i - index == 1:
                    q.append(p[index])
                index = i
            i += 1
        if index == len(p)-1:
            q.append(p[-1])
        if len(q) == len(p):
            flag = False
        else:
            p = q
    return q

for line in sys.stdin:
    line = line[:-1]
    p = [i for i in line]
    minLen = len(line)
    for i in xrange(len(p)+1):
        for c in "ABC":
            temp = copy.deepcopy(p)
            temp.insert(i, c)
            q = dele(temp)
            if len(q) < minLen:
                minLen = len(q)
    print(len(line)+1-minLen)
