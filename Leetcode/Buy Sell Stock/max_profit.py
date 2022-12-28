class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        if len(prices) == 0: return None

        # Tabulation array generation
        buy_arr = [0] * len(prices)
        profit_arr = [0] * len(prices)

        # Base case value initialization
        buy_arr[0] = prices[0]
        profit_arr[0] = 0
        
        for i in range(1, len(prices)):

            # Handles finding minimum buy price
            buy_arr[i] = min(prices[i], buy_arr[i - 1])
            
            # Handles finding maximum profit price
            profit = prices[i] - buy_arr[i] 
            profit_arr[i] = max(profit, profit_arr[i - 1])

        return profit_arr[-1]