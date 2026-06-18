class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min_sofar = prices[0]
        max_sofar = float('-inf')
        profit = 0



        for right in range(1,len(prices)):

            profit = max(profit , prices[right]-min_sofar)   

            min_sofar = min(min_sofar , prices[right])

        return profit      