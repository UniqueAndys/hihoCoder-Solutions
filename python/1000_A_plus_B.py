import sys

for line in sys.stdin:
    l = [int(x) for x in line.split()]
    print(l[0]+l[1])
