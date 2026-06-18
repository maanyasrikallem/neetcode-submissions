class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:

        left = 1
        right = max(piles)

        ans = right 

        while left <= right :

            hour = 0

            mid = (left+right) // 2

            for i in range(len(piles)) :

                hour += (piles[i] + mid - 1)//mid
            
            if hour > h :
                left = mid + 1
            else :
                right = mid - 1
            

        return left 
