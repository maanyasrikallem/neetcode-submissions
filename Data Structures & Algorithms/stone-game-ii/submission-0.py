class Solution:
    def stoneGameII(self, piles: List[int]) -> int:

        n = len(piles)

        dp = [[float('-inf')]*(n+1) for _ in range(n+1)]

        for M in range(n + 1):
            dp[n][M] = 0


        for i in range(n-1,-1,-1):

            for M in range(n , 0 ,-1):

                cur = 0

                for x in range(1,min(2*M , n-i)+1):
                    cur += piles[i+x-1]
                    dp[i][M] = max(
                        dp[i][M] , cur - dp[i+x][max(M,x)]
                    )

        total = sum(piles)
        diff = dp[0][1]

        return (total+diff)//2 
            
