class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        min_height = n 
        res = []

        graph = defaultdict(list)

        for a,b in edges :

            graph[a].append(b)
            graph[b].append(a)
        
        def height(node,visited) :

            visited.add(node)

            h = 0 

            for child in graph[node] :
                if child in visited :
                    continue 
                visited.add(child)
                h = max(h , 1+height(child,visited))

            return h 

        
        for i in range(n) :

            min_height = min(min_height , height(i,set()))

        for i in range(n) :

            if height(i,set()) == min_height :
                res.append(i)

        return res







