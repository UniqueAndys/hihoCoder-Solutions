'''
贪心策略
最长连续提交区间 必然是借助补提交卡将其中连续的未打卡日期补交得到
遍历有限情况即可
'''
num = raw_input()
for i in xrange(int(num)):
    line1 = raw_input()
    line2 = raw_input()
    n, m = [int(x) for x in line1.split()]
    days = [int(x) for x in line2.split()]
    if m >= n:
        print(100)
    else:
        days.append(101)
        max_day = days[m] - 1
        for i in xrange(n-m):
            if days[i+m+1] - days[i] - 1 > max_day:
                max_day = days[i+m+1] - days[i] - 1
        print(max_day)
