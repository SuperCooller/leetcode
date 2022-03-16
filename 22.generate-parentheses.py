#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#

# @lc code=start
class Solution:
    def generateParenthesis1(self, n: int) -> List[str]:
        if n == 0:
            return ['']
        if n == 1:
            return ["()"]
        ans = [] 
        for c in range(n):
            for left in self.generateParenthesis1(c):
                for right in self.generateParenthesis1(n - c - 1):
                    ans.append("({}){}".format(left, right))
        return ans
    
    def generateParenthesis2(self, n: int) -> List[str]:
        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                ans.append(''.join(S))
                return 
            if left < n:
                S.append('(')
                backtrack(S, left+1, right)
                S.pop() 
            if right < left:
                S.append(")")
                backtrack(S, left, right+1)
                S.pop() 
        backtrack([], 0, 0)
        return ans
    
    def generateParenthesis(self, n: int) -> List[str]:
        if n == 0:
            return []
        total_l = []
        total_l.append([None])
        total_l.append(["()"])
        for i in range(2, n+1):
            l = []
            for j in range(i):
                left_list = total_l[j]
                right_list = total_l[i-1-j]
                for left in left_list:
                    for right in right_list:
                        if left is None:
                            left = ""
                        if right is None:
                            right = ""
                        l.append("({}){}".format(left, right))
            total_l.append(l)
        return total_l[n]
        
# @lc code=end

