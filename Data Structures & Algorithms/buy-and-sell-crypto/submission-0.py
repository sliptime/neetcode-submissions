class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProfits = [0] * len(prices)

        minPrice = prices[0]
        for i, price in enumerate(prices):
            maxProfits[i] = price - minPrice
            minPrice = min(minPrice, price)

        return max(maxProfits)
