class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:
        self.perim = 0
        m = len(grid)
        n = len(grid[0])
        visited = set()
        def dfs(i,j):
            if (i,j) in visited :
                return 
            if i < 0 or i >= m or j < 0 or j >= n :
                self.perim += 1 
                return

            if grid[i][j] == 0 :
                
                self.perim += 1
                return 
            else:
                visited.add((i,j))
                dfs(i-1,j)
                dfs(i,j-1)
                dfs(i+1,j)
                dfs(i,j+1)

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1:
                    dfs(i,j)
                    return self.perim

        return self.perim 

        
        