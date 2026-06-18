class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        parent = [i for i in range(len(edges)+1)]

        def union(a,b):

            pa = find(a)
            pb = find(b)

            if pa == pb:
                return False 

            parent[pa] = pb 

            return True 
        
        def find(a):
            if parent[a] != a:
                parent[a] = find(parent[a])
            return parent[a]
            
        for a,b in edges :
            if not union(a,b):
                return [a,b]
            
            



            




        