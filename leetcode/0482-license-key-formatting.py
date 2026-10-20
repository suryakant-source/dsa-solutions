class Solution:
    def licenseKeyFormatting(self, s: str, k: int) -> str:
        t = s.replace("-", "").upper()
        first = len(t) % k
        parts = []
        if first:
            parts.append(t[:first])
        for i in range(first, len(t), k):
            parts.append(t[i:i + k])
        return "-".join(parts)
