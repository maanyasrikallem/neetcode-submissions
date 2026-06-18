class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy = sell = cooldown = 0

        for i in range(len(prices) - 1, -1, -1):
            new_buy = max(buy, -prices[i] + sell)
            new_sell = max(sell, prices[i] + cooldown)
            new_cooldown = buy

            buy = new_buy
            sell = new_sell
            cooldown = new_cooldown

        return buy