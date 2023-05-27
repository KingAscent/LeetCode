var generate = function(numRows) {
    let pas = [];

    for(let i = 0; i < numRows; i++){
        pas[i] = new Array(i + 1);
        pas[i][0] = 1;
        pas[i][i] = 1;
        for(let j = 1; j < i; j++){
            pas[i][j] = pas[i - 1][j - 1] + pas[i - 1][j];
        }
    }

    return pas;
};
