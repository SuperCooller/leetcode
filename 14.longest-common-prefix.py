#
# @lc app=leetcode id=14 lang=python3
#
# [14] Longest Common Prefix
#

# @lc code=start
class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0]) 
        min_s = strs[0]
        for i in range(1, len(strs)):
            l = len(strs[i])
            if l < min_len:
                min_len = l 
                min_s = strs[i]
        common_prefix = ""
        for index, c in enumerate(min_s):
            is_common = True 
            for s in strs:
                if s[index] != c:
                    is_common = False 
            if is_common:
                common_prefix += c 
            else:
                break
        return common_prefix 
        
# @lc code=end

