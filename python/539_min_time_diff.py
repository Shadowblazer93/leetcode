def findMinDifference(timePoints):
    res = float('inf')
    time = sorted([int(i[:2])*60+int(i[3:]) for i in timePoints])
    print(time)
    for k in range(1,len(time)):
        res = min(res, time[k]-time[k-1])
    res = min(res, 1440+time[0]-time[-1])
    return res
print(findMinDifference(["23:59","00:00","11:39"]))