class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        dict_t = {}
        for strs in t:
            if strs in dict_t :
                dict_t[strs] += 1
            else:
                dict_t[strs] = 1
        
        dict_s = {}
        for strs in s:
            if strs in dict_s :
                dict_s[strs] += 1
            else:
                dict_s[strs] = 1

        if dict_s == dict_t:
            return True
        else:
            return False

        

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna