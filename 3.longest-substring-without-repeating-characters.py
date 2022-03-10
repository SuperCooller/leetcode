#
# @lc app=leetcode id=3 lang=python3
#
# [3] Longest Substring Without Repeating Characters
#

# @lc code=start
class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_len = 0
        begin = -1
        h_map = {} 
        for i, c in enumerate(s):
            last_index = h_map.get(c, -1)
            t_max = -1
            if last_index < begin:
                t_max = i - begin + 1 
            else:
                t_max = i - last_index 
                begin = last_index + 1 
            if t_max > max_len:
                max_len = t_max 
            h_map[c] = i
        return max_len 
                
# @lc code=end

