class Solution:
    def canPartitionKSubsets(self, nums: List[int], k: int) -> bool:

        total = sum(nums)

        if total % k != 0:
            return False

        target = total // k

        nums.sort(reverse=True)

        buckets = [0] * k

        def bt(idx):

            if idx == len(nums):
                return True

            for i in range(k):

                if buckets[i] + nums[idx] > target:
                    continue

                buckets[i] += nums[idx]

                if bt(idx + 1):
                    return True

                buckets[i] -= nums[idx]

                # pruning: avoid trying identical empty buckets
                if buckets[i] == 0:
                    break

            return False

        return bt(0)