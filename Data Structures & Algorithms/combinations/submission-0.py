class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:

        nums = [i+1 for i in range(n)]

        res = []
        path = []

        def bt(idx) :

            if len(path) == k:
                res.append(path[:])

            for i in range(idx , n):

                path.append(nums[i])

                bt(i+1)

                path.pop()

        bt(0)
        return res        