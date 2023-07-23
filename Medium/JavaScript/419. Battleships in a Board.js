var countBattleships = function(board) {
    let count = 0;
    let r = board.length;
    let c = board[0].length;

    for(let i = 0; i < r; i++){
        for(let j = 0; j < c; j++){
            if(board[i][j] == 'X'){
                if((i == r - 1 || board[i + 1][j] == '.') &&
                   (j == c - 1 || board[i][j + 1] == '.'))
                    count++;
            }
        }
    }

    return count;
};
