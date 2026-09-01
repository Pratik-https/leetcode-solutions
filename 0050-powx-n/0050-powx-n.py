class Solution:
 def findPow(self,x,n):
  # base case
  if n == 0:
    return 1
  if n == 1:
    return x
  # recursive case
  a = self.findPow(x,n//2)
  if n%2 == 1:
    return a*a*x
  else:
    return a*a

 def myPow(self,x,n):
  if n>=0:
    return self.findPow(x,n)
  else:
    n *= -1
    return 1/self.findPow(x,n)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna