class Solution(object):
    def maxProfit(self, prices):
        start = prices[0]
        maxprof = 0
        for i in range(1, len(prices)):
            if prices[i] > start:
                maxprof += prices[i] - start
                start = prices[i]
            else:
                start = prices[i]
        return maxprof


if __name__ == "__main__":
    prices =[7, 1, 5, 3, 6, 4]
    solution = Solution()
    solution.maxProfit(prices)