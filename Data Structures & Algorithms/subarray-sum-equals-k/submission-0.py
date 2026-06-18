class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        freq = {0: 1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum += num

            if cur_sum - k in freq:
                count += freq[cur_sum - k]

            freq[cur_sum] = freq.get(cur_sum, 0) + 1

        return count