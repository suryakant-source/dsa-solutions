# LeetCode 225. Implement Stack using Queues
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 09:10 IST
# Pattern: Rotate the queue on push so front is the top.
# Complexity: O(n) push, O(1) pop/top.

from collections import deque

class MyStack:
    def __init__(self): self.q=deque()
    def push(self, x):
        self.q.append(x)
        for _ in range(len(self.q)-1): self.q.append(self.q.popleft())
    def pop(self): return self.q.popleft()
    def top(self): return self.q[0]
    def empty(self): return not self.q
