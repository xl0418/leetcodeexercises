class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """

        nrow = len(board)
        ncol = len(board[0])

        ones_id = []

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] == 1:
                    ones_id.append((i, j))

        czeros_id = []
        cones_id = []
        for i in range(nrow):
            for j in range(ncol):
                neighbour_pop = 0
                for ones in [(i-1, j), (i-1, j-1), (i-1, j+1), (i, j-1), (i, j+1), (i+1, j-1), (i+1, j), (i +1, j+1)]:
                    if ones in ones_id:
                        neighbour_pop += 1
                if neighbour_pop<2:
                    czeros_id.append([i, j])

                if board[i][j] == 1 and neighbour_pop == 2:
                    cones_id.append([i, j])

                if neighbour_pop == 3:
                    cones_id.append([i, j])

                if neighbour_pop > 3:
                    czeros_id.append([i, j])

        for zeroij in czeros_id:
            board[zeroij[0]][zeroij[1]] = 0

        for oneij in cones_id:
            board[oneij[0]][oneij[1]] = 1

board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
solution = Solution()
solution.gameOfLife(board)