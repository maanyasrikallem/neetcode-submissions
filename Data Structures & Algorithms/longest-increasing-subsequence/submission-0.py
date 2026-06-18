class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        dp = [float('-inf')] * (n+1)

        for i in range(n):
            for j in range(i):
                if nums[j] < nums[i] :
                    dp[i] = max(dp[i] , 1+dp[j])
            if dp[i] == float('-inf'):
                dp[i] = 1 

        return max(dp)

        