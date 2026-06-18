class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        n = len(nums)
        k%=n

        if n == 1 :
            return 
        
        count = 0
        start = 0

        while count < n :

            current = start
            prev = nums[start]

            while True :

                next_ind = (current+k)%n
                nums[next_ind] , prev = prev , nums[next_ind]
                current = next_ind
                count+=1

                if current == start :
                    break

            start+=1             

