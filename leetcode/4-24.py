# LeetCode 24. Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Accepted as Suryakant_16 on 2026-11-17 16:31:25 IST (55/55 testcases)
# Practice solution written with AI assistance for daily DSA practice

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: ListNode | None) -> ListNode | None:
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            a = prev.next
            b = a.next
            a.next = b.next
            b.next = a
            prev.next = b
            prev = a
        return dummy.next
