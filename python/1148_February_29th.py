'''
快速计算两个年份之间闰年的个数
'''
n = int(raw_input())

monthDict = {"January":1, "February":2, "March":3, "April":4,
             "May":5, "June":6, "July":7, "August":8,
             "September":9, "October":10, "November":11, "December":12}

def isRun(year):
    if (year%4==0 and year%100!=0) or (year%400==0):
        return True
    return False

def contain(start, end, digit):
    # [start, end)
    num = 0
    a = start % digit
    b = end % digit
    # 边界情况
    if a != 0:
        start -= a
        num -= 1
    if b != 0:
        end += (digit-b)
    num += (end-start)/digit
    return num

def numYear(start, end):
    num = 0
    num += contain(start, end, 4)
    num -= contain(start, end, 100)
    num += contain(start, end, 400)
    return num

for i in xrange(n):
    start = raw_input().split(" ")
    start[1] = int(start[1][:-1])
    start[2] = int(start[2])
    end = raw_input().split(" ")
    end[1] = int(end[1][:-1])
    end[2] = int(end[2])

    num = numYear(start[2], end[2])
    if isRun(start[2]) and monthDict[start[0]]>2:
        num -= 1
    if isRun(end[2]):
        if monthDict[end[0]]>2 or (monthDict[end[0]]==2 and end[1]==29):
            num += 1
    print "Case #" + str(i+1) + ": " + str(num)
