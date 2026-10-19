# LeetCode 150. Evaluate Reverse Polish Notation
# Difficulty: Medium
# Status: Accepted (Python3)
# Solved: Oct 16, 2026 08:09 IST
# Pattern: Stack; pop two on operator, push result. Division truncates toward zero.
# Complexity: O(n) time, O(n) space.

class Solution:
    def evalRPN(self, tokens):
        stack=[]
        for t in tokens:
            if t not in ('+','-','*','/'):
                stack.append(int(t))
                continue
            b,a=stack.pop(),stack.pop()
            if t=='+': v=a+b
            elif t=='-': v=a-b
            elif t=='*': v=a*b
            else: v=(abs(a)//abs(b))*(-1 if (a<0)!=(b<0) else 1)
            stack.append(v)
        return stack[0]
