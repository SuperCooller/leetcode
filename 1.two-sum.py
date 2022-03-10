#
# @lc app=leetcode id=1 lang=python3
#
# [1] Two Sum
#

# @lc code=start
class Solution:
    def twoSum(self, nums, target):
        h_map = {} 
        for i, n in enumerate(nums):
            c = target - n 
            if c in h_map:
                return [i, h_map[c]] 
            h_map[n] = i
# @lc code=end

