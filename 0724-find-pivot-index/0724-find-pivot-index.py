class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        n = len(nums)
        total_sum = sum(nums)
        left_sum = 0

        for i in range(n):
            right_sum = total_sum - left_sum - nums[i]
            if right_sum == left_sum:
                return i
            left_sum += nums[i]
        return -1
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna