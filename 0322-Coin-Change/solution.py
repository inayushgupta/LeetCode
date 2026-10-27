class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:

        dp = [float('inf')] * (amount+1)

        for total_amount in range(1, len(dp)):

            for coin in coins:

                required_amount = total_amount - coin
                if required_amount < 0:
                    break
                
                dp[total_amount] = min(dp[required_amount] + 1, dp[total_amount])

        
        return dp[-1]