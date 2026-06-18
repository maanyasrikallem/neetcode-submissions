class Solution:
    def candy(self, ratings: List[int]) -> int:

        n = len(ratings)

        candies = [1] *n

        for i in range(n-1) :
            if ratings[i+1] > ratings[i] :
                candies[i+1] = candies[i] + 1 

        for j in range(n-1,0,-1):
            if ratings[j-1] > ratings[j] and (not candies[j-1] > candies[j]):
                candies[j-1] = candies[j] + 1

        return sum(candies)
            


        