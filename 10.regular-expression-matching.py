#
# @lc app=leetcode id=10 lang=python3
#
# [10] Regular Expression Matching
#

# @lc code=start
class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        s_len = len(s)
        p_len = len(p)
        m = [[False for _ in range(p_len + 1)] for _ in range(s_len+1)]
        m[0][0] = True 

        def match(s, p, i, j):
            if i == 0:
                return False 
            if p[j-1] == '.':
                return True 
            return s[i-1] == p[j-1]

        for i in range(s_len + 1):
            # i, j is the length of sub_s and sub_p
            for j in range(1, p_len+1):
                if p[j-1] == '*':
                    m[i][j] |= m[i][j-2]
                    if match(s, p, i, j-1):
                        m[i][j] |= m[i-1][j] 
                else:
                    if match(s, p, i, j):
                        m[i][j] |= m[i-1][j-1]
        return m[s_len][p_len]

    def isMatchRec(self, s: str, p: str) -> bool:
        return self.isMatchP(s, 0, p, 0)

    def isMatchP(self, s, s_start, p, p_start):
        s_len = len(s) 
        p_len = len(p)
        if p_start >= p_len:
            return s_start >= s_len 
        if p_start == p_len - 1:
            if s_start != s_len - 1:
                return False
            return p[p_start] == '.' or p[p_start] == s[s_start]
        if p[p_start + 1] != '*':
            if s_start >= s_len:
                return False
            if p[p_start] == s[s_start] or p[p_start] == '.':
                return self.isMatchP(s, s_start + 1, p, p_start + 1) 
            else:
                return False 
        else:
            while s_start < s_len and (p[p_start] == s[s_start] or (p[p_start] == '.' and s_start < s_len)):
                if self.isMatchP(s, s_start, p, p_start+2):
                    return True 
                s_start += 1 
            return self.isMatchP(s, s_start, p, p_start + 2)


        
# @lc code=end

