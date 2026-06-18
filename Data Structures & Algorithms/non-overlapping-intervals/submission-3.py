class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        def is_overlap(a,b):
            return a[0] < b[1] and b[0] < a[1]
        n = len(intervals)
        intervals.sort(key = lambda x:  x[1])

        res = [intervals[0]]
        count = 0

        i = 1
        while i < n:
            while i < n and intervals[i][0] < res[-1][1]:
                count+=1 
                i+=1 

            if i < n :
                res.append(intervals[i])
                i+=1

        return count

        