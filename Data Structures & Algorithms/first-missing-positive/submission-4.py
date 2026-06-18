class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        min_num = min(nums)
        if min_num > 1:
            return 1
        
        else:
            
            a = 1
            while a in set(nums):
                a = a+1
            return a 
