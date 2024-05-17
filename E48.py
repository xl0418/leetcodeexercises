class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """

        n = len(matrix)
        if n == 1:
            return matrix

        for row in range(n):
            for col in range(row, n):
                matrix[row][col], matrix[col][row] = matrix[col][row], matrix[row][col]

        for i in range(n):
            left, right = 0, n -1
            while left < right:
                matrix[i][left], matrix[i][right] = matrix[i][right], matrix[i][left]
                left += 1
                right -= 1





matrix = [[1,2,3],[4,5,6],[7,8,9]]
solution = Solution()
solution.rotate(matrix)