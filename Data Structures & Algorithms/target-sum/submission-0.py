class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        
        dp = defaultdict(int)
        dp[0] = 1

        for num in nums :
            
            new_dp = defaultdict(int)

            for x,count in dp.items():

                new_dp[x+num] += count
                new_dp[x-num] += count 
            
            dp = new_dp

        return dp[target]


                

