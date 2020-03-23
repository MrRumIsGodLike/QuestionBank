class Solution:
    def CheckPermutation(self, s1: str, s2: str) -> bool:
        # 排序法
        return sorted(s1) == sorted(s2)