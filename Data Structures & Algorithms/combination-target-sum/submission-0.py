class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        path = []

        def bt(i) :

            if sum(path) > target :
                return 

            if sum(path) == target :
                res.append(path[:])

            for i in range(i,len(nums)) :

                path.append(nums[i])

                bt(i)

                path.pop()

        bt(0)
        return res
        