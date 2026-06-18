class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:

        heap = []

        for i in range(len(nums)):
            heapq.heappush(heap , nums[i])
        i = 0
        while heap and i<len(nums):
            nums[i] = heapq.heappop(heap)
            i+=1

        return nums

        