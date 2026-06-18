class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        components = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()

        def dfs(i,j):
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == '0' :
                return 

            if (i,j) in visited :
                return 
            
            visited.add((i,j))
            
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)
 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1' and (i,j) not in visited :
                    dfs(i,j)
                    components += 1 

        return components 
        