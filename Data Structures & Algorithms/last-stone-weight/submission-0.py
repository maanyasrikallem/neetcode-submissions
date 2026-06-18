class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        max_heap = []

        for stone in stones :

            heapq.heappush(max_heap , -stone)

        while len(max_heap) > 1:

            x = - heapq.heappop(max_heap)
            y = - heapq.heappop(max_heap)

            if x > y :
                heapq.heappush(max_heap , y - x)
            elif y>x :
                heapq.heappush(max_heap , x - y)

        if max_heap :
            return -max_heap[0]
        else:
            return 0

        
            

 
        