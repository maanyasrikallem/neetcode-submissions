class Solution:
    def getOrder(self, tasks: List[List[int]]) -> List[int]:

        n = len(tasks)

        # (enqueueTime, processingTime, originalIndex)
        tasks = [(e, p, i) for i, (e, p) in enumerate(tasks)]

        tasks.sort()

        heap = []
        res = []

        time = 0
        i = 0

        while i < n or heap:

            # If no available task, jump to the next enqueue time
            if not heap and time < tasks[i][0]:
                time = tasks[i][0]

            # Add all available tasks
            while i < n and tasks[i][0] <= time:

                enqueue, process, idx = tasks[i]

                heapq.heappush(heap, (process, idx))

                i += 1

            # Execute the shortest task
            process, idx = heapq.heappop(heap)

            time += process

            res.append(idx)

        return res