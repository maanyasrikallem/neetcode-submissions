class Solution:
    def findMinHeightTrees(self, n: int, edges: List[List[int]]) -> List[int]:

        q = deque()
        degree = [0]*n

        if n == 1:
            return [0]

        graph = defaultdict(list)

        for a,b in edges :

            graph[a].append(b)
            degree[a]+=1
            graph[b].append(a)
            degree[b]+=1 
        
        remaining = n

        for i in range(n) :    
            if degree[i] == 1 :
                q.append(i)
        
        while remaining > 2 :

            size = len(q)

            remaining -= size 

            for _ in range(size):
                    
                leaf = q.popleft()

                for nei in graph[leaf] :
                    degree[nei] -= 1

                    if degree[nei] == 1 :
                        q.append(nei)

        return list(q)


        



