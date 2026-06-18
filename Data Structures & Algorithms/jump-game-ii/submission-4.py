class Solution:
    def jump(self, nums: List[int]) -> int:

        count = 0
        n = len(nums)
        right = 0
        left = 0
        farthest = 0

        while right < len(nums) - 1:

            for i in range(left, right+1):
                farthest = max(farthest , i + nums[i])

            left = right + 1
            right = farthest 
            count += 1 

        return count

            
        