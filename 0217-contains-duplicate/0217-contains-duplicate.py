class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        set1 = set({})

        for num in nums:
            if num in set1:
                return True
            set1.add(num)
        return False

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna