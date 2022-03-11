#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0:
            return False 
        x = abs(x) 
        abs_x = x
        rev_x = 0 
        while x != 0:
            x, pop = divmod(x, 10)
            rev_x = rev_x * 10 + pop 
        if rev_x == abs_x:
            return True 
        return False 
        
# @lc code=end

