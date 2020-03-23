class Solution:
    def isFlipedString(self, s1: str, s2: str) -> bool:
        # 1.极简
        return len(s1) == len(s2) and s1 in s2 * 2
