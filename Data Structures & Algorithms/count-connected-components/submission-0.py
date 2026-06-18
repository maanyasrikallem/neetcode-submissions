class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:

        graph  = [[] for _ in range(n)]
        comp = 0
        visited = set()

        for a,b in edges :
            graph[a].append(b)
            graph[b].append(a)

        def dfs(x):
            visited.add(x)

            for nei in graph[x]:
                if nei not in visited :
                    dfs(nei)


        for i in range(n):
            if i not in visited :
                comp += 1
                dfs(i)

        return comp 

        
        