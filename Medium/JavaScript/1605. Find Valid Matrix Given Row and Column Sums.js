var restoreMatrix = function(rowSum, colSum) {
    const mat = new Array(rowSum.length);
    for(let i = 0; i < rowSum.length; i++)
        mat[i] = new Array(colSum.length);
    
    // Fill each spot of the matrix by finding the min of
    // rowSum[i] and colSum[j], then place it into the
    // matrix. Subtract mat[i][j] from rowSum[i]
    // and colSum[j]
    for(let i = 0; i < rowSum.length; i++){
        for(let j = 0; j < colSum.length; j++){
            mat[i][j] = Math.min(rowSum[i], colSum[j]);
            rowSum[i] -= mat[i][j];
            colSum[j] -= mat[i][j];
        }
    }

    return mat;
};
