#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        curr = head = ListNode()
        carry = 0
        
        while l1 or l2:
            v1, v2 = 0, 0
            if l1:
                v1, l1 = l1.val, l1.next
            if l2:
                v2, l2 = l2.val, l2.next
            
            sum = v1 + v2 + carry
            carry = 1 if sum >= 10 else 0
            curr.next = ListNode(sum % 10)
            curr = curr.next
        if carry:
            curr.next = ListNode(1)
        
        return head.next
            
# @lc code=end

