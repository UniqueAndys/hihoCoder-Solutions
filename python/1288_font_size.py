'''
先计算一个上界，即不考虑边界条件、段落换行的最大字体，然后逐渐减小。
'''
m = int(raw_input())

def upper_bound(m, n):
    if m % n == 0:
        return m / n
    else:
        return (m / n) + 1

def page(size, w, h, a):
    # given a size, how many pages needed
    w_s = w / size
    h_s = h / size
    num = 0
    for a_i in a:
        # upper bound
        num += upper_bound(a_i, w_s)
    return upper_bound(num, h_s)

for i in xrange(m):
    n, p, w, h = [int(x) for x in raw_input().split()]
    a = [int(x) for x in raw_input().split()]
    maxSize = (h*p*w/sum(a))**(1./2)
    j = int(maxSize)
    flag = True
    while j > 0 and flag:
        if j <= min(w,h) and page(j, w, h, a) <= p:
            print j
            flag = False
        j -= 1
