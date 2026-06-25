class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        min_height = n 
        res = []
        heights = defaultdict(list)

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

            h = height(i,set())

            heights[h].append(i)

            min_height = min(min_height , h)


        return heights[min_height]







