class SubrectangleQueries {
    
    // Initialize the matrix
    int[][] matrix;
    public SubrectangleQueries(int[][] rectangle) {
        matrix = rectangle;
    }
    
    public void updateSubrectangle(int row1, int col1, int row2, int col2, int newValue) {
        // Assign every value in the matrix to the newValue
        // Upper left coordinate is (row1, col1)
        // Lower right coordinate is (row2, col2)
        for(int i = row1; i <= row2; i++){
            for(int j = col1; j <= col2; j++){
                matrix[i][j] = newValue;
            }
        }
    }
    
    public int getValue(int row, int col) {
        return matrix[row][col];
    }
}
