class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:

        heap = []
        count = 0

        zipped = []

        for p , cap in zip(profits , capital ) :

            zipped.append((p,cap))
        
        zipped.sort(key = lambda x: x[1])

        capital = w
        i = 0

        while count < k :

            while i < len(zipped) :
                if zipped[i][1] > capital :
                    break

                heapq.heappush(heap , -zipped[i][0])
                i+=1

            if not heap or count >= k:
                return capital 

            capital -= heapq.heappop(heap)
            count += 1 

        return capital
 




        