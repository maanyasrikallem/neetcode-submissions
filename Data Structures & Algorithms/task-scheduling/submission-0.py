class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:

        freq = Counter(tasks)
        
        cooldown = deque()

        heap = [-ct for ct in freq.values()]
        heapq.heapify(heap)
        
        time = 0

        while heap or cooldown :

            time += 1

            if heap :

                cnt = 1 + heapq.heappop(heap)

                if cnt != 0 :

                    cooldown.append((time+n , cnt))


            if cooldown and time == cooldown[0][0] :

                _ , cnt = cooldown.popleft()

                heapq.heappush(heap , cnt)

        return time



        