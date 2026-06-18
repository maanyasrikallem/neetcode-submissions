class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        sofar = {}
        nums.sort()
        maxim = 0

        for num in nums:
            if num-1 in sofar:
                sofar[num] = sofar[num-1]+1
            else:
                sofar[num] = 1
            

            maxim = max(maxim , sofar[num])

        return maxim

        

            

        

        