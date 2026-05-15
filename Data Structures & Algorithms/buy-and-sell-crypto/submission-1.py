class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = 0
        minPrice = prices[0]
        for i, price in enumerate(prices):
            maxProfits = max(maxProfits, price - minPrice)
            minPrice = min(minPrice, price)

        return maxProfits
