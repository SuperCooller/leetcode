#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        len_1 = len(nums1)
        len_2 = len(nums2) 
        if (len_1 + len_2) % 2 != 0:
            return self.findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (len(nums1) + len(nums2)) // 2 + 1)
        return (self.findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (len(nums1) + len(nums2)) // 2) \
                    + self.findKth(nums1, 0, len(nums1)-1, nums2, 0, len(nums2)-1, (len(nums1) + len(nums2)) // 2 + 1)) / 2.
    
    def findKth(self, nums1, start1, end1, nums2, start2, end2, kth):
        len_1 = end1 - start1 + 1
        len_2 = end2 - start2 + 1
        if len_1 < len_2:
            return self.findKth(nums2, start2, end2, nums1, start1, end1, kth) 
        if len_2 == 0:
            return nums1[start1 + kth - 1]
        if kth == 1:
            return min(nums1[start1], nums2[start2]) 

        mid_index = kth // 2 
        i2 = mid_index if mid_index < len_2 else len_2
        i1 = kth - i2
        n1 = nums1[start1 + i1 - 1]
        n2 = nums2[start2 + i2 - 1]
        if n1 == n2:
            return n1
        elif n1 < n2:
            return self.findKth(nums1, start1 + i1, end1, nums2, start2, end2, kth-i1)
        else:
            return self.findKth(nums1, start1, end1, nums2, start2+i2, end2, kth-i2)
# @lc code=end

