#
# @lc app=leetcode id=20 lang=python3
#
# [20] Valid Parentheses
#

# @lc code=start
class Solution:
    def isValid(self, s: str) -> bool:
        m = {'(': ')', '{': '}', '[': ']'}
        stack = [] 
        for ch in s:
            if ch in m:
                stack.append(ch) 
            else:
                if not stack or m[stack[-1]] != ch:
                    return False
                stack.pop() 
        return not stack 

# @lc code=end

