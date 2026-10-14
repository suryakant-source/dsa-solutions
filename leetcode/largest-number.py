from functools import cmp_to_key

class Solution:
    def largestNumber(self, nums):
        def cmp(a, b):
            return (a+b < b+a) - (a+b > b+a)
        a = sorted(map(str, nums), key=cmp_to_key(cmp))
        return '0' if a[0] == '0' else ''.join(a)
