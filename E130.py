class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        if len(board) != 0:
            nrow = len(board)
            ncol = len(board[0])
            o_pos = [[1 if board[x][y] == "O" else 0 for y in range(ncol)] for x in range(nrow)]
            for irow in range(nrow):
                for icol in range(ncol):
                    if board[irow][icol] == "O":
                        if 'X' in board[irow][:icol] and 'X' in board[irow][icol:]:
                            col_val = [board[x][icol] for x in range(nrow)]
                            if 'X' in col_val[:irow] and 'X' in col_val[irow:]:
                                board[irow][icol] = "X"
                                o_pos[irow][icol] = 2

        if nrow > 2 and ncol > 2:
            do = True
            while do:
                bool_vec = [False]
                for irow in range(1, nrow-1):
                    for icol in range(1, ncol-1):
                        if o_pos[irow][icol] == 2:
                            if o_pos[irow][icol-1] == 1 or o_pos[irow][icol+1] == 1 or o_pos[irow+1][icol] == 1 or o_pos[irow-1][icol] == 1:
                                board[irow][icol] = 'O'
                                o_pos[irow][icol] = 1
                                bool_vec.append(True)

                if any(bool_vec):
                    continue
                else:
                    do = False





board = [["O","X","O","O","X","X"],["O","X","X","X","O","X"],["X","O","O","X","O","O"],["X","O","X","X","X","X"],["O","O","X","O","X","X"],["X","X","O","O","O","O"]]
solution = Solution()
solution.solve(board)