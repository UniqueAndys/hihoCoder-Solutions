x, y, z = [int(i) for i in raw_input().split()]
s = raw_input()


def diff(ball, x, y, z):
    a = abs(ball[0]-ball[1])
    b = abs(ball[1]-ball[2])
    c = abs(ball[2]-ball[0])
    d1 = sorted([a, b, c])
    d2 = sorted([x, y, z])
    for i in xrange(len(d1)):
        if d1[i] != d2[i]:
            return False
    return True

num = 0
ball = [0, 0, 0]
max_num = 0
for c in s:
    if c == "R":
        ball[0] += 1
    elif c == "Y":
        ball[1] += 1
    else:
        ball[2] += 1
    num += 1
    if diff(ball, x, y, z):
        if num > max_num:
            max_num = num
        num = 0
        ball = [0, 0, 0]
print max(max_num, num)
