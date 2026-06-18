class Solution:
    def canJump(self, nums: List[int]) -> bool:

        left = 0
        right = nums[0]
        
        n = len(nums)

        if right >= n -1:
            return True 

        if n==1 :
            return True 
        new_right = float('-inf')

        while right < n-1 and left < right :
            i = left + 1

            while i <= right  :
                
                if i + nums[i] > right :
                    new_right = i + nums[i]

                    if new_right >= n-1 :
                        return True 
                i+=1

            left = right 
            if new_right != float('-inf') :
                right = new_right 

        return False 
        