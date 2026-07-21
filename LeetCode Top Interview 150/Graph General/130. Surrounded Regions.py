from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        # Step1:iterate all border cells
        for i in range(len(board)):
            self.dfs(board, i, 0)
        for i in range(len(board)):
            self.dfs(board, i, len(board[0]) - 1)
        for j in range(len(board[0])):
            self.dfs(board, 0, j)
        for j in range(len(board[0])):
            self.dfs(board, len(board) - 1, j)

        # Step2 Replace all surrounded cells with X
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":#we should first replace O with X, Otherwise the following replacement will replace island O
                    board[i][j] = "X"
                elif board[i][j] == "E":
                    board[i][j] = "O"

    def dfs(self, board, x, y):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]):
            return
        if board[x][y] != "O":
            return
        board[x][y] = "E"
        self.dfs(board, x + 1, y)
        self.dfs(board, x, y + 1)
        self.dfs(board, x - 1, y)
        self.dfs(board, x, y - 1)


if __name__ == '__main__':
    solution = Solution()
    board = [["X", "O", "X", "O", "X", "O"], ["O", "X", "O", "X", "O", "X"], ["X", "O", "X", "O", "X", "O"],
             ["O", "X", "O", "X", "O", "X"]]
    for i in range(len(board)):
        print(board[i])
    print(solution.solve(board))
    for i in range(len(board)):
        print(board[i])
