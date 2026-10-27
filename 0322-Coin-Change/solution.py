class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [0] + [float("inf")] * amount
        coins.sort()

        for total_amount in range(1, len(dp)):

            for coin in coins:

                required_amount = total_amount - coin
                if required_amount < 0:
                    break

                dp[total_amount] = min(dp[required_amount] + 1, dp[total_amount])

        return dp[-1] if dp[-1] != float("inf") else -1
