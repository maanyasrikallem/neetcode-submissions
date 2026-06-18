class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]:

        graph = [[] for _ in range(numCourses)]

        for a,b in prerequisites :
            graph[a].append(b)

        def dfs(i,j,visited):
            if i == j :
                return True 

            visited.add(i)

            for nei in graph[i]:
                if nei not in visited :
                    if dfs(nei,j,visited):
                        return True 



            return False 

        
        ans = []

        for u,v in queries :
            ans.append(dfs(u,v,set()))

        return ans 