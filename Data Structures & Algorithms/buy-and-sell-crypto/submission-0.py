class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        cheapest = prices[0]
        mp = 0
        f, s = 0, 0

        while f < len(prices):
            if prices[f] < cheapest:
                s = f
                cheapest = prices[f]
            elif (prices[f] - prices[s]) > mp:
                mp = prices[f] - prices[s]
                f += 1
            else:
                f += 1
        return mp