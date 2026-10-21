class Solution:
    def busyStudent(self, startTime: list[int], endTime: list[int], queryTime: int) -> int:
        return sum(1 for a, b in zip(startTime, endTime) if a <= queryTime <= b)
