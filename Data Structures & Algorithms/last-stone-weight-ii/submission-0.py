class Solution:
    def lastStoneWeightII(self, stones: List[int]) -> int:

        n = len(stones)

        total = sum(stones)
        target = total//2

        dp = [False] * (target+1)
        dp[0] = True

        for stone in stones :
            for i in range(target , stone-1 , -1):
                dp[i] = dp[i] or dp[i-stone]

        for i in range(target , -1 , -1):
            if dp[i]:
                return total - 2*i 

        