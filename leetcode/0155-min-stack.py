# LeetCode 155. Min Stack
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 08:32 IST
# Pattern: Stack of (value, running minimum) pairs.
# Complexity: O(1) per operation.

class MinStack:
    def __init__(self): self.stack=[]
    def push(self, value): self.stack.append((value,min(value,self.stack[-1][1]) if self.stack else value))
    def pop(self): self.stack.pop()
    def top(self): return self.stack[-1][0]
    def getMin(self): return self.stack[-1][1]
