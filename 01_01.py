class Solution:
    def isUnique(self, astr: str) -> bool:
        # 1.字典筛选
        # 2.set (AC)
        # a = set(astr)
        # if len(a) == len(astr):
        #     return True
        # else:
        #     return False
        # 3.位运算
        mark = 0
        for char in astr:
            move = ord(char) - ord('a')
            if (mark & (1 << move)) != 0:
                return False
            else:
                mark |= (1 << move)
        return True