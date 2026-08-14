class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = strs[0]

        for i in range(len(prefix)):
            for j in range(1, len(strs)):
                if i == len(strs[j]) or strs[j][i] != prefix[i]:
                    return prefix[:i]

        return prefix
        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna