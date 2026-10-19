# LeetCode 206. Reverse Linked List
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 22:34 IST
# Pattern: Iterative pointer reversal.
# Complexity: O(n) time, O(1) space.

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        prev = None
        while head:
            head.next, prev, head = prev, head, head.next
        return prev
