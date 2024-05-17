class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        maxprofit = 0
        temp_profit = 0
        for i in range(len(prices) - 1):
            temp_profit += prices[i+1] - prices[i]
            temp_profit = max(temp_profit, 0)
            maxprofit = max(maxprofit, temp_profit)

        return maxprofit






if __name__ == "__main__":
    prices = [7,1,5,3,6,4]
    res = Solution()
    ret = res.maxProfit(prices)

