#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        head = dummy = ListNode()
        while list1 is not None or list2 is not None:
            if list1 is None:
                head.next = list2
                list2, head = list2.next, list2
            elif list2 is None:
                head.next = list1
                list1, head = list1.next, list1
            else:
                if list1.val < list2.val:
                    head.next = list1
                    list1, head = list1.next, list1
                else:
                    head.next = list2 
                    list2, head = list2.next, list2
        return dummy.next

# @lc code=end

