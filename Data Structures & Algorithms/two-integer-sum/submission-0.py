class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        done = {}

        for i,num in enumerate(nums):
            if target-num in done :
                return [done[target-num] , i]

            done[num] = i 


        