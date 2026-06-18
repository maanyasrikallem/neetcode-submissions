class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:

        n = len(nums)

        res  =[]

        nums.sort()

        for (idx,k) in enumerate(nums) :

            if idx > 0 and nums[idx] == nums[idx - 1]:
                continue
            left = idx+1
            right = n-1
            while left < right :
                if nums[left] + nums[right] > -k :
                    right -= 1
                elif nums[left] + nums[right] < -k :
                    left += 1
                else:
                    res.append([k,nums[left],nums[right]])
                    left += 1
                    right -= 1

                    while left < right and nums[left] == nums[left-1]:
                        
                        left+=1

                    while left < right and nums[right] == nums[right+1]:
                        
                        right-=1

        return res
                
        