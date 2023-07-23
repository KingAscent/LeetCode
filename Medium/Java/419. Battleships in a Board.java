class Solution {
    public int countBattleships(char[][] board) {
        int count = 0;
        int r = board.length;
        int c = board[0].length;

        for(int i = 0; i < r; i++){
            for(int j = 0; j < c; j++){
                if(board[i][j] == 'X'){
                    if((i == r - 1 || board[i + 1][j] == '.') &&
                       (j == c - 1 || board[i][j + 1] == '.'))
                        count++;
                }
            }
        }

        return count;
    }
}
