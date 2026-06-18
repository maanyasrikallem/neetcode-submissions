class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        n = len(nums)
        slow = 0

        for fast in range(1,n):
            if nums[fast] != nums[fast-1]:
                nums[slow] = nums[fast-1]
                slow+=1
        nums[slow] = nums[n-1] 

            

        return slow+1


        