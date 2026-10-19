# LeetCode 148. Sort List
# Difficulty: Medium
# Status: Accepted (Python3)
# Pattern: sort linked list by extracting values, sorting, writing back.
# Complexity: O(n log n) time, O(n) space for the values array.
# Interview recall:
# - The follow-up asks O(1) space: bottom-up merge sort on the list itself.
# - Value rewrite is simpler and accepted; relinking nodes is the classic answer.
# - Edge: empty list and single node return as-is.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: ListNode | None) -> ListNode | None:
        vals = []
        node = head
        while node:
            vals.append(node.val)
            node = node.next
        vals.sort()
        node = head
        for v in vals:
            node.val = v
            node = node.next
        return head
