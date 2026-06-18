class Solution:
    def findMin(self, nums: List[int]) -> int:

        n = len(nums)

        left = 0
        right = len(nums) - 1

        while left <= right :

            mid = (left+right) // 2
            
            if nums[mid] > nums[n-1] :
                left = mid + 1
            else :
                right = mid - 1

        return nums[left] 
        