class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:

        path = []
        res = []

        def bt(idx) :

            res.append(path[:])

            for i in range(idx,len(nums)) :

                path.append(nums[i])

                bt(i+1)

                path.pop()


        bt(0)
        return res 