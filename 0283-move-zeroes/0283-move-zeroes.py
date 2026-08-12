class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        n = len(nums)
        start = 0

        for i in range(n):
            if nums[i] != 0:
                nums[start],nums[i] = nums[i],nums[start]
                start += 1
        
        return nums
            
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna