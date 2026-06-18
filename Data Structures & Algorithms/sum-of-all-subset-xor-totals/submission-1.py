class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        def bt(i , xor) :

            if i == len(nums) :
                return xor

            return (
                bt(i+1,xor) + bt(i+1 , xor^nums[i])
            )


        return bt(0 ,0)