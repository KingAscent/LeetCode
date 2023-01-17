var rotate = function(matrix) {
        for(let i = 0; i < Math.floor((matrix.length + 1) / 2); i++){
            for(let j = 0; j < Math.floor(matrix.length / 2); j++){
                let temp = matrix[i][j];
                matrix[i][j] = matrix[matrix.length - j - 1][i];
                matrix[matrix.length - j - 1][i] = matrix[matrix.length - i - 1][matrix.length - j - 1];
                matrix[matrix.length - i - 1][matrix.length - j - 1] = matrix[j][matrix.length - i - 1];
                matrix[j][matrix.length - i - 1] = temp;
            }
        }
};

