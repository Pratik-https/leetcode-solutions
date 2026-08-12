class Solution(object):
    def maxProfit(self, prices):
        min_price = prices[0]
        ans = 0

        for price in prices[1:]:
            min_price = min(min_price, price)
            curr_profit = price - min_price
            ans = max(ans, curr_profit)

        return ans
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna