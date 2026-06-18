class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:

        def is_overlap(a,b):
            return a[0] <= b[1] and b[0] <= a[1]

        intervals.sort(key = lambda x : (x[0],x[1]))
        
        res = [intervals[0]]
        n = len(intervals)

        for interval in intervals[1:]:
            if is_overlap(res[-1] , interval):                
                merged = [
                    min(res[-1][0], interval[0]),
                    max(res[-1][1], interval[1])
                ]
                
                res.pop()
                res.append(merged)
            
            else:
                res.append(interval)

        return res
            