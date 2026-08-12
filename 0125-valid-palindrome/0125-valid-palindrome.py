class Solution(object):
    def isAlpha(self,s):
        x = ord(s)

        if 97 <= x <= 122 or 48 <= x <= 57:
            return True
        else:
            return False

    def isPalindrome(self, s):
        n = len(s)
        s = s.lower()
        i,j = 0,n-1

        while i < j:
            if not self.isAlpha(s[i]):
                i += 1
            
            elif not self.isAlpha(s[j]):
                j -= 1

            elif s[i] != s[j]:
                return False

            else:
                i += 1
                j -= 1
        
        return True


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna