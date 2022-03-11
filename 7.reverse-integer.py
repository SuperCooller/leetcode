#
# @lc app=leetcode id=7 lang=python3
#
# [7] Reverse Integer
#

# @lc code=start
class Solution:
    def reverse(self, x: int) -> int:
        int_max = 2 ** 31 - 1
        int_min = - 2 ** 31 
        max_d = int_max // 10
        res = 0
        while x != 0:
            x, pop = self.divmod_v2(x, 10) 
            if res > max_d or (res == int_max // 10 and pop > 7):
                return 0 
            if res < -max_d or (res == int_min // 10 and pop < -8):
                return 0 
            res = res * 10 + pop 
        return res 
        
    def divmod_v2(self, a, b):
        res, pop = divmod(abs(a), b)
        flag = 1 if a > 0 else -1
        return res * flag, pop * flag

        
# @lc code=end

