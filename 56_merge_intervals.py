
def merge(intervals):
    if not intervals:
        return []

    intervals = sorted(intervals)
    si = intervals[0][0]
    ei = intervals[0][1]

    res = []
    for i in range(1, len(intervals)):
        if ei >= intervals[i][0]:
            if ei < intervals[i][1]:
                ei = intervals[i][1]
        else:
            res.append([si, ei])
            si = intervals[i][0]
            ei = intervals[i][1]

    res.append([si, ei])
    return res

# print(merge([[1,3],[2,6],[8,10],[15,18]]))

print(merge([[1,4],[2,3]]))
