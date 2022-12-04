var SubrectangleQueries = function(rectangle) {
    matrix = rectangle;
};

SubrectangleQueries.prototype.updateSubrectangle = function(row1, col1, row2, col2, newValue) {
    // Assign every value in the matrix to the newValue
    // Upper left coordinate is (row1, col1)
    // Lower right coordinate is (row2, col2)
    for(let i = row1; i <= row2; i++){
        for(let j = col1; j <= col2; j++){
            matrix[i][j] = newValue;
        }
    }
};

SubrectangleQueries.prototype.getValue = function(row, col) {
    return matrix[row][col];
};
