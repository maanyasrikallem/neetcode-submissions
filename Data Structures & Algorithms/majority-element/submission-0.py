class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        freq = {}
        n = len(nums)

        for i in range(len(nums)):
            if nums[i] not in freq:
                freq[nums[i]] = 0
            freq[nums[i]]+=1

            if freq[nums[i]] > n//2 :
                return nums[i]
        