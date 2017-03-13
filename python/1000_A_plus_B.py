'''
逐行读取两个数，相加即可
'''
import sys

for line in sys.stdin:
    l = [int(x) for x in line.split()]
    print(l[0]+l[1])
