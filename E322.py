class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        if amount == 0: return 0

        dp = [float("inf") for _ in range(amount + 1)]
        dp[0] = 0

        for denom in coins:
            for i in range(1, len(dp)):
                if i >= denom:
                    dp[i] = min(dp[i], 1 + dp[i - denom])

        return dp[-1] if dp[-1] != float("inf") else -1


coins = [186,419,83,408]
amount = 6249
solution = Solution()
solution.coinChange(coins, amount)
