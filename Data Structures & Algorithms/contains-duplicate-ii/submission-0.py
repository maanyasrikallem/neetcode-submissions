class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        
        n = len(nums)
        left = 0

        seen = set()
        
        for right in range(n):

            if right-left > k :
                seen.remove(nums[left])
                left+=1

            if nums[right] in seen :
                return True 
            else :
                seen.add(nums[right])

        return False 

            
            


            
        