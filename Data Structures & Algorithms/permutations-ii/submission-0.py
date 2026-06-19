class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:

        res = []
        path = []
        visited = set()
        nums.sort()

        def bt(idx):

            if len(path) == len(nums) :
                res.append(path[:])
                return 

            for i in range(len(nums)):

                if i>0 and nums[i] == nums[i-1] and i-1 not in visited:
                    continue 
                if i in visited:
                    continue 

                
                path.append(nums[i])
                visited.add(i)

                bt(i+1)

                path.pop()
                visited.remove(i)

        bt(0)
        return res
        