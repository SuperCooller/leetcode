#
# @lc app=leetcode id=5 lang=python3
#
# [5] Longest Palindromic Substring
#

# @lc code=start
class Solution:
    
    def longestPalindrome_time_exceeded(self, s: str) -> str:
        #Status: Time Limit Exceeded
        s_len = len(s)
        m = [[False for _ in range(s_len)] for _ in range(s_len)]
        max_len = 1
        start = 0
        for i in range(s_len):
            m[i][i] = True 
            if i + 1 < s_len:
                if s[i] == s[i+1]:
                    m[i][i+1] = True 
                    if 2 > max_len:
                        max_len = 2
                        start = i
        for l in range(3, s_len+1):
            for i in range(s_len):
                if i + l - 1 >= s_len:
                    continue 
                if m[i+1][i+l-2] and (s[i] == s[i+l-1]):
                    m[i][i+l-1] = True
                    if l > max_len:
                        max_len = l     
                        start = i
        return s[start: start + max_len] 

    # https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
    def longestPalindrome_expand_around_center(self, s: str) -> str:
        if s is '': 
            return s
        max_len = 0 
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.expandFromCenter(s, i, i)
            len2 = self.expandFromCenter(s, i, i+1)
            l = max(len1, len2)
            if l > end - start:
                start = i - (l - 1) // 2
                end = i + l // 2

        return s[start:end+1]

    def expandFromCenter(self, s, idx1, idx2):
        while idx1 >= 0 and idx2 < len(s) and s[idx1] == s[idx2]:
            idx1 -= 1
            idx2 += 1
        return idx2 - idx1 - 1 

    # https://zkf85.github.io/2019/03/26/leetcode-005-longest-palindrome
    def longestPalindrome(self, s: str) -> str:
        N = len(s) 
        if N < 2: 
            return s
        N = 2*N+1    # Position count 
        L = [0] * N 
        L[0] = 0
        L[1] = 1
        C = 1     # centerPosition 
        R = 2     # centerRightPosition 
        i = 0    # currentRightPosition 
        iMirror = 0     # currentLeftPosition 
        maxLPSLength = 0
        maxLPSCenterPosition = 0
        start = -1
        end = -1
        diff = -1
   
        for i in range(2, N): 
            # get currentLeftPosition iMirror for currentRightPosition i 
            iMirror = 2*C-i 
            L[i] = 0
            diff = R - i 
            # If currentRightPosition i is within centerRightPosition R 
            if diff > 0: 
                L[i] = min(L[iMirror], diff) 
   
            # Attempt to expand palindrome centered at currentRightPosition i 
            # Here for odd positions, we compare characters and 
            # if match then increment LPS Length by ONE 
            # If even position, we just increment LPS by ONE without 
            # any character comparison 
            try:
                while ((i + L[i]) < N and (i - L[i]) > 0) and \
                    (((i + L[i] + 1) % 2 == 0) or \
                    (s[(i + L[i] + 1) // 2] == s[(i - L[i] - 1) // 2])): 
                    L[i]+=1
            except Exception as e:
                pass
                
            if L[i] > maxLPSLength:        # Track maxLPSLength 
                maxLPSLength = L[i] 
                maxLPSCenterPosition = i 
   
            # If palindrome centered at currentRightPosition i 
            # expand beyond centerRightPosition R, 
            # adjust centerPosition C based on expanded palindrome. 
            if i + L[i] > R: 
                C = i 
                R = i + L[i] 
   
        start = (maxLPSCenterPosition - maxLPSLength) // 2
        end = start + maxLPSLength - 1
        return s[start:end+1]
        
# @lc code=end

