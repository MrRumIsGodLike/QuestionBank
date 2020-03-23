class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        # 1.常规解法
        # N = len(matrix)
        # # 沿着主对角线交换
        # for i in range(N):
        #     for j in range(i):
        #         matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # for i in range(N):
        #     matrix[i] = matrix[i][::-1]
        # 2.异或计算
        # https://blog.csdn.net/lewky_liu/article/details/85219084
        n = len(matrix)
        for i in range(n):
            matrix[i].reverse()
        for i in range(n):
            for j in range(n - i):
                if matrix[i][j] == matrix[n - j - 1][n - i - 1]:
                    continue
                matrix[i][j] = matrix[i][j] ^ matrix[n - j - 1][n - i - 1]
                matrix[n - j - 1][n - i - 1] = matrix[i][j] ^ matrix[n - j - 1][n - i - 1]
                matrix[i][j] = matrix[i][j] ^ matrix[n - j - 1][n - i - 1]

