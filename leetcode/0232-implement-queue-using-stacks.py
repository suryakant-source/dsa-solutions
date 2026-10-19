# LeetCode 232. Implement Queue using Stacks
# Difficulty: Easy
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 08:55 IST
# Pattern: In-stack and out-stack; transfer only when out is empty.
# Complexity: O(1) amortized per operation.

class MyQueue:
    def __init__(self): self.ins=[];self.out=[]
    def push(self, x): self.ins.append(x)
    def transfer(self):
        if not self.out:
            while self.ins: self.out.append(self.ins.pop())
    def pop(self):
        self.transfer()
        return self.out.pop()
    def peek(self):
        self.transfer()
        return self.out[-1]
    def empty(self): return not self.ins and not self.out
