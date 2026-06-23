class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        heap = []
        cap = 0

        trips.sort(key = lambda x : x[1])

        for memb , fro , to in trips :

            while heap and fro >= heap[0][0] :

                _ , ppl = heapq.heappop(heap)
                cap -= ppl 
            
            cap += memb 

            if cap > capacity :
                return False 

            heapq.heappush(heap , (to , memb))

        return True 
        