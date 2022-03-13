#
# @lc app=leetcode id=15 lang=python3
#
# [15] 3Sum
#

# @lc code=start
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        num_length = len(nums)
        result = []
        if num_length < 3:
            return result
        nums.sort() 
        for i, n_i in enumerate(nums):
            if i > 0 and nums[i] == nums[i-1]:
                continue 
            for j in range(i+1, num_length-1):
                if nums[i] + nums[j] + nums[j+1] > 0:
                    break 
                if j > i + 1 and nums[j] == nums[j-1]:
                    continue 
                k = num_length - 1
                while k > j and (nums[i] + nums[j] + nums[k] > 0):
                    k -= 1
                if j == k:
                    break 
                if nums[i] + nums[j] + nums[k] == 0:
                    result.append([nums[i], nums[j], nums[k]])
        return result

        
# @lc code=end

