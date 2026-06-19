class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []

        def bt(idx) :

            if len(path) == len(nums) :
                res.append(path[:])
                return 

            for i in range(len(nums)) :

                if nums[i] in path:
                    continue 
                path.append(nums[i])

                bt(i+1)

                path.pop()

        bt(0)

        return res
        