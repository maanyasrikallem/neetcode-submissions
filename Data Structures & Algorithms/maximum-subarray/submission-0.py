class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur = 0
        for i in range(len(nums)) :
            cur += nums[i]

            nums[i] = max(cur ,nums[i] )
            cur = nums[i]

        return max(nums)
        