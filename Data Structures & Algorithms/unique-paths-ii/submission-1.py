class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        
        dp = [[0]*n for _ in range(m)]
        if obstacleGrid[0][0] == 1 or obstacleGrid[m-1][n-1]:
            return 0

        for i in range(m) :
            for j in range(n):

                if i==0 and j==0:
                    dp[i][j] = 1
                    continue 

                if j-1 >= 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] += dp[i][j-1]
                
                if i-1 >= 0 and obstacleGrid[i][j] != 1:
                    dp[i][j] += dp[i-1][j]

        return dp[m-1][n-1] 