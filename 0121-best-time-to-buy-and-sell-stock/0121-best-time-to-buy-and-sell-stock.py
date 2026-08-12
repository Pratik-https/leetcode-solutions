class Solution(object):
    def maxProfit(self, prices):
        n = len(prices)
        min_price = prices[0]
        ans = 0

        for i in range(1,n):
            min_price = min(min_price,prices[i])
            curr_profit = prices[i] - min_price
            ans = max(ans,curr_profit)
        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna