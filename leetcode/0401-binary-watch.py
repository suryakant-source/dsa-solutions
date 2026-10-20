class Solution:
    def readBinaryWatch(self, turnedOn: int) -> list[str]:
        res = []
        for h in range(12):
            for m in range(60):
                if bin(h).count("1") + bin(m).count("1") == turnedOn:
                    res.append(str(h) + ":" + ("0" if m < 10 else "") + str(m))
        return res
