class Solution:
    def numSquares(self, n: int) -> int:

        dp = [float('inf')]*(n+1)
        count = 0
        squares = []
        i = 0

        while i*i <= n :
            squares.append(i*i)
            dp[i*i] = 1
            i+=1 

        for num in squares :
            for i in range(num , n+1):
                dp[i] = min(dp[i] , 1 + dp[i-num])

        return dp[n]
        
                   
        



        