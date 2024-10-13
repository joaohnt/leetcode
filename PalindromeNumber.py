class Solution(object):
    def isPalindrome(self, x):
        x = str(x)
        s1=""
        for char in x:
              s1 += char

        s2 = ""
        for char in reversed(x):
             s2 += char

        if s1 == s2:
             return True;

solution = Solution()
x = -121
print(solution.isPalindrome(x))