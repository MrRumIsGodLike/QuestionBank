class Solution:
    def oneEditAway(self, first: str, second: str) -> bool:
        # 插入、删除、替换
        # 最多需要一次编辑操作
        # 1.编辑距离？？？
        # 2.双指针 分长度不同和长度相同两种情况
        if abs(len(first) - len(second)) >= 2:
            return False

        count = 0
        if len(first) == len(second):
            for i in range(len(first)):
                if first[i] != second[i]:
                    count += 1
                    if count == 2:
                        return False
            return True

        if len(first) < len(second):
            first, second = second, first

        for i in range(len(first)):
            if first[0:i] + first[i + 1:] == second:
                return True
        return False

