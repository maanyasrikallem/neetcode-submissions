class Solution:
    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:

        intervals.sort()
        res = [float('inf')]*len(queries)

        for ind,q in enumerate(queries):

            for i in intervals:

                if i[0] <= q <= i[1] :
                    res[ind] = min(res[ind] , i[1]-i[0]+1)

        for index,x in enumerate(res):
            if x== float('inf'):
                res[index] = -1

        return res



                    
        