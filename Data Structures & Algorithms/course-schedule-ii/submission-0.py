class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
        graph = [[] for _ in range(numCourses)]
        indegree = [0] * numCourses
        q = deque()
        path = []

        for a, b in prerequisites:
            graph[b].append(a)
            indegree[a] += 1

        for i in range(numCourses):
            if indegree[i] == 0:
                q.append(i)

        taken = 0

        while q:
            node = q.popleft()
            path.append(node)
            taken += 1

            for nei in graph[node]:
                indegree[nei] -= 1

                if indegree[nei] == 0:
                    q.append(nei)

        if taken != numCourses:
            return []
        else:
            return path 