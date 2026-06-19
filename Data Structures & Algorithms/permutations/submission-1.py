class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        visited = [False]*len(nums)

        def bt() :

            if len(path) == len(nums) :
                res.append(path[:])
                return 

            for i in range(len(nums)) :

                if visited[i] :
                    continue 

                path.append(nums[i])
                visited[i] = True

                bt()

                path.pop()
                visited[i] = False

        bt()

        return res
        