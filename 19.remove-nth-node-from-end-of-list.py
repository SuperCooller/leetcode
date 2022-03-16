#
# @lc app=leetcode id=19 lang=python3
#
# [19] Remove Nth Node From End of List
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        h, x = head, 0
        while h:
            x += 1
            h = h.next
        z = x - n + 1
        if z == 1: return head.next
        h = head
        for i in range(1, z-1):
            h = h.next
        h.next = h.next.next
        return head

# @lc code=end

