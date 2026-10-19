# LeetCode 21. Merge Two Sorted Lists
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 15, 2026 22:55 IST
# Pattern: Two-pointer merge into a dummy head.
# Complexity: O(n+m) time, O(1) space.

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        d = t = ListNode()
        while list1 and list2:
            if list1.val <= list2.val:
                t.next = list1; list1 = list1.next
            else:
                t.next = list2; list2 = list2.next
            t = t.next
        t.next = list1 or list2
        return d.next
