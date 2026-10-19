# LeetCode 141. Linked List Cycle
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 21:54 IST
# Pattern: Floyd tortoise and hare.
# Complexity: O(n) time, O(1) space.

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        s = f = head
        while f and f.next:
            s = s.next; f = f.next.next
            if s is f: return True
        return False
