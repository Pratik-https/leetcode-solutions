class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        n = len(nums)
        dict = {}

        for i in range(n):
            if nums[i] in dict:
                dict[nums[i]] += 1
            else:
                dict[nums[i]] = 1
            
            if dict[nums[i]] >= 2:
                return True
        return False
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna