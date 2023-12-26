class Solution:
    def isPalindrome(self, x: int) -> bool:
        # convert to a string:
        cts = str(x)
        # string reversal! 
        if cts == cts[::-1]:
            return True
        else:
            return False

question1 = Solution()
x = 121
result = question1.isPalindrome(x)
print(result)

question2 = Solution()
x = -121
result = question2.isPalindrome(x)
print(result)

question3 = Solution()
x = 10
result = question3.isPalindrome(x)
print(result)