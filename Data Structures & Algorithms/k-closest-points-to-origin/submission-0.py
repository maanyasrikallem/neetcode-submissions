class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:

        def dist(x,y):
            return x**2 + y **2 

        heap = []

        for p in points :

            heapq.heappush(heap , (-dist(p[0],p[1]) , p))

            if len(heap) > k :
                heapq.heappop(heap)

        return [p for d,p in heap]



        