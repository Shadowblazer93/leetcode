def minGroups(intervals:list):
    groups = []
    intervals.sort()
    L = list(intervals)

    while intervals:
        grp = [intervals[0]]
        intervals.pop(0)
        
        for i in L:
            if i[0]>grp[-1][1]:
                grp.append(i)
                if i in intervals: intervals.remove(i)
    
        groups.append(grp)

    return groups

#print(minGroups([[5,10],[6,8],[1,5],[2,3],[1,10]]))
print(minGroups([[1,3],[5,6],[8,10],[11,13]]))