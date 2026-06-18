class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:

        n = len(nums)

        tails = []

        tails.append(nums[0])

        for i in range(1,n):
            if nums[i] > tails[-1]:
                tails.append(nums[i])

            else:
                x = len(tails)
                left = 0
                right = x-1

                while left <= right :
                    mid = (left+right)//2

                    if tails[mid] >= nums[i] :
                        right = mid-1
                    else:
                        left = mid+1

                tails[left] = nums[i]

        return len(tails)



        