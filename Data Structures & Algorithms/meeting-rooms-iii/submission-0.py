class Solution:
    def mostBooked(self, n: int, meetings: List[List[int]]) -> int:
        meetings.sort()

        available = list(range(n)) 
        occupied = []
        
        heapq.heapify(available)

        count = [0]*n

        for start , end in meetings :
            duration = end - start 

            while occupied and occupied[0][0] <= start :
                _ , room = heapq.heappop(occupied)
                heapq.heappush(available , room)

            if available :
                room = heapq.heappop(available)
                heapq.heappush(occupied , (end , room))

            else:
                free_time , room = heapq.heappop(occupied)
                heapq.heappush(occupied , (free_time+duration , room))
            

            count[room] += 1

        return count.index(max(count))