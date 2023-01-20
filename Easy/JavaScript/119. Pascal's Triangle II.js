var getRow = function(rowIndex) {
    let row = [];

    for(let i = 0; i <= rowIndex; i++){
        row[i] = [];
        row[i][0] = 1;
        for(let j = i - 1; 0 < j; j--){
            row[i][j] = row[i - 1][j - 1] + row[i - 1][j];
        }
        row[i][i] = 1;
    }

    return row[rowIndex];
};
