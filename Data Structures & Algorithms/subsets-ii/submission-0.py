class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        nums.sort()

        def bt(idx):

            res.append(path[:])

            for i in range(idx , len(nums)):

                if i>idx and nums[i] == nums[i-1]:
                    continue 

                path.append(nums[i])

                bt(i+1)

                path.pop()

        bt(0)
        return res
        