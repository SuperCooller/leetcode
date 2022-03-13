#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        h_len = len(height) 
        max_area = 0 
        left = 0 
        right = h_len - 1
        while left < right:
            area = min(height[left], height[right]) * (right - left)
            if area > max_area:
                max_area = area 
            if left < right:
                left += 1
            else:
                right -= 1
        return max_area 
        
# @lc code=end

