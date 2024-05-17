class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        if not matrix:
            return []

        left, right, top, bottom = 0, len(matrix[0])-1, 0, len(matrix)-1
        result = []

        while len(result) < len(matrix) * len(matrix[0]):

            for rows in range(left, right+1):
                result.append(matrix[top][rows])
            top += 1

            for cols in range(top, bottom+1):
                result.append(matrix[cols][right])
            right -= 1

            if top <= bottom:
                for i in range(right, left-1, -1):
                    result.append(matrix[bottom][i])
                bottom -= 1

            if left <= right:
                for i in range(bottom, top -1, -1):
                    result.append(matrix[i][left])
                left += 1

        return result





matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
solution = Solution()
solution.spiralOrder(matrix)
