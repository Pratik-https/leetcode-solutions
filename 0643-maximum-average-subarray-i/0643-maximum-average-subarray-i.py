class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        n = len(nums)
        curr_sum = 0
        for i in range(k):
            curr_sum += nums[i]
        ans = curr_sum / k

        for i in range(k,n):
            curr_sum += nums[i]
            curr_sum -= nums[i-k]
            curr_avg = curr_sum / k
            ans = max(ans,curr_avg)
        return ans


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna