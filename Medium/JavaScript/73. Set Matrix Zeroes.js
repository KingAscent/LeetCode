var setZeroes = function(matrix) {
    let row = Array(matrix.length);
    let col = Array(matrix[0].length);

    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(matrix[i][j] == 0){
                row[i] = true;
                col[j] = true;
            }
        }
    }

    for(let i = 0; i < matrix.length; i++){
        for(let j = 0; j < matrix[0].length; j++){
            if(row[i] || col[j])
                matrix[i][j] = 0;
        }
    }
};
