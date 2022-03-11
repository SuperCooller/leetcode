#
# @lc app=leetcode id=8 lang=python3
#
# [8] String to Integer (atoi)
#

# @lc code=start
class Solution:
    def myAtoi(self, s: str) -> int:
        flag = 1
        res = 0
        is_begin = 0
        for c in s.strip():
            if not is_begin and c == "-" and flag == 1:
                flag = -1
                is_begin = 1
                continue
            if not is_begin and c == "+":
                is_begin = 1
                continue
            if c not in '0123456789':
                break
            n = int(c)
            if n >= 0 and n <= 9:
                is_begin = 1
                res = res * 10 + n 
        res = flag * res 
        if res > 2 ** 31 - 1:
            res = 2 ** 31 - 1
        if res < - 2 ** 31:
            res = - 2 ** 31
        return res 

        
# @lc code=end

