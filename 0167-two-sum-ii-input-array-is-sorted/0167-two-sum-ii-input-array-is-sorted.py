class Solution(object):
    def twoSum(self, numbers, target):
        n = len(numbers)
        i,j = 0,n-1

        while i < j:
            sum = numbers[i] + numbers[j]
            if sum > target:
                j -= 1
            elif sum < target:
                i += 1
            else:
                return [i+1,j+1]
        return [-1,-1]  
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna