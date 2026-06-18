class Solution:
    def splitArray(self, nums: List[int], k: int) -> int:

        left = max(nums)
        right = sum(nums)

        while left <= right :

            mid = (left+right) // 2

            i = 0

            count = 0

            while i < len(nums) :

                cur_sum = 0

                while i < len(nums) and nums[i] + cur_sum <= mid :

                    cur_sum += nums[i]
                    i+=1 

                count += 1

            if count <= k :
                right = mid - 1
            else :
                left = mid + 1

        return left 
                




        