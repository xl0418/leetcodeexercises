class Solution:
    def setZeroes(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        nrow = len(matrix)
        ncol = len(matrix[0])

        row_ind = []
        col_ind = []
        for i in range(nrow):
            for j in range(ncol):
                if matrix[i][j] == 0:
                    row_ind.append(i)
                    col_ind.append(j)

        for r in row_ind:
            matrix[r] = [0 for _ in range(ncol)]

        for c in col_ind:
            for r in range(nrow):
                matrix[r][c] = 0



matrix = [[1,1,1],[1,0,1],[1,1,1]]

solution = Solution()
solution.setZeroes(matrix)