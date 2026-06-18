class Solution:
    def shipWithinDays(self, weights: List[int], days: int) -> int:

        left = max(weights)
        right = sum(weights)
        

        while left <= right :

            day = 0

            mid = (left+right) // 2

            i=0

            while i < len(weights) :

                cur_sum = 0

                while i<len(weights) and weights[i] + cur_sum <= mid :
                    cur_sum += weights[i]
                    i+=1 

                day += 1

            if day > days :
                left = mid + 1
            else :
                right = mid - 1

        return left 


        