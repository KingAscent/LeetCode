class Solution(object):
    def countBattleships(self, board):
        count = 0
        r = len(board)
        c = len(board[0])

        for i in range(r):
            for j in range(c):
                if board[i][j] == 'X':
                    if (i == r - 1 or board[i + 1][j] == '.') and (j == c - 1 or board[i][j + 1] == '.'):
                        count += 1

        return count
