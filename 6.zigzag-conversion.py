#
# @lc app=leetcode id=6 lang=python3
#
# [6] Zigzag Conversion
#

# @lc code=start
class Solution:
    def convert(self, s: str, numRows: int) -> str:
        # be carefull for numRows = 1
        if numRows == 1:
            return s
        res_arr = ['' for _ in range(numRows)] 
        index = 0
        arrow = 1
        for i, c in enumerate(s):
            res_arr[index] += c 
            if index == numRows - 1 and arrow == 1:
                arrow = -1
            elif index == 0 and arrow == -1:
                arrow = 1 
            index = index + arrow 
        res = ''
        for s in res_arr:
            res += s 
        return res 
# @lc code=end

