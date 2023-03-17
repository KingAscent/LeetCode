var generateMatrix = function(n) {
    let mat = Array(n);
    for(let i = 0; i < mat.length; i++)
        mat[i] = Array(n);

    let temp = 1;
    let row = 0;
    let rowEnd = n - 1;
    let col = 0;
    let colEnd = n - 1;

    while(temp <= n * n){
        // Shift from left to right
        for(let i = col; i <= colEnd; i++){
            mat[row][i] = temp;
            temp++;
        }
        row++;

        // Shift from top to bot
        for(let i = row; i <= rowEnd; i++){
            mat[i][colEnd] = temp;
            temp++;
        }
        colEnd--;

        // Shift from right to left
        for(let i = colEnd; col <= i; i--){
            mat[rowEnd][i] = temp;
            temp++;
        }
        rowEnd--;

        // Shift from bot to top
        for(let i = rowEnd; row <= i; i--){
            mat[i][col] = temp;
            temp++;
        }
        col++;
    }

    return mat;
};
