var transpose = function(matrix) {
    const newMatrix = [];

    for(let i = 0; i < matrix[0].length; i++){
        const temp = [];
        for(let j = 0; j < matrix.length; j++){
            temp.push(matrix[j][i]);
        }
        newMatrix.push(temp);
    }

    return newMatrix;
};
