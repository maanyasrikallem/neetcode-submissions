class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:

        total = 0
        path = []
        

        def bt(i) :

            nonlocal total

            if i == len(nums):


                cur_xor = 0

                for i in path :
                    cur_xor ^= i
                total += cur_xor 
                return 

            path.append(nums[i])
            bt(i+1)
            path.pop()
            bt(i+1)

        bt(0)

        return total
        