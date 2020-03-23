class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1.记录零元素的行列元组
        n = len(matrix)
        m = len(matrix[0])
        tmp = []
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    tmp.append((i, j))
        for i, j in tmp:
            for k in range(n):
                matrix[k][j] = 0
            for l in range(m):
                matrix[i][l] = 0

