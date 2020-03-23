class Solution:
    def isPower(self,n):
        if n < 1:
            return False
        i = 1
        while i <= n:
            if i == n:
                return True
            i <<= 1
        return False

    def canPermutePalindrome(self, s: str) -> bool:
        # 哈希表/Counter数据结果
        # 位运算: 奇数的字符个数为0或1
        mark = 0
        for c in s:
            move = ord(c)
            mark ^= 1 << move
        # 分别判断奇偶
        return  mark == 0 or self.isPower(mark)