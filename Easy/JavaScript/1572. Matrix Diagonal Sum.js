var diagonalSum = function(mat) {
    let sum = 0;
    let top = 0;
    let bot = mat[0].length - 1;

    // Subtract the value of any secondary diagonal
    if(mat[0].length % 2 == 1)
        sum -= mat[bot / 2][bot / 2];
    
    // Add each value from the matrix diagonals
    for(let i = 0; i < mat[0].length; i++){
        sum += mat[i][top] + mat[i][bot];
        top++;
        bot--;
    }

    return sum;    
};
