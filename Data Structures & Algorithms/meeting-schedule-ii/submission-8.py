"""
Definition of Interval:
class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end
"""

class Solution:
    def minMeetingRooms(self, intervals: List[Interval]) -> int:

        intervals.sort(key = lambda x : x.start)

        if not intervals :
            return 0
        
        room = 1
        q = []
        heapq.heappush(q , intervals[0].end)

        for interval in intervals[1:] :

            if interval.start >= q[0] :
                
                heapq.heappop(q)
                heapq.heappush(q , interval.end)
                continue 
            else:
                room +=1 
                heapq.heappush(q , interval.end)
                

        return room 
        
        