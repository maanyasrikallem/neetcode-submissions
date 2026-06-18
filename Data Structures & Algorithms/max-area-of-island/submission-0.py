class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        
        max_area = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(i,j):

            
            
            if i < 0 or j < 0 or i >= m or j >= n or grid[i][j] == 0 :
                return 

            grid[i][j] = 0
            self.cur_area+=1
            
            dfs(i-1,j)
            dfs(i,j-1)
            dfs(i+1,j)
            dfs(i,j+1)

            return self.cur_area 
 
        
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 :
                    self.cur_area = 0
                    area = dfs(i,j)
                    max_area = max(max_area,area) 

        return max_area 
        

        
        