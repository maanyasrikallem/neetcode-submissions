class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:

        n = len(nums)
        nums = nums 
        ans = [1]*n

        for i in range(1,n):
            ans[i] = ans[i-1] * nums[i-1] 
        
        
        right = 1
        for j in range(n-2 ,-1,-1):
            right *= nums[j+1]
            ans[j]  *= right

        return ans



            
        