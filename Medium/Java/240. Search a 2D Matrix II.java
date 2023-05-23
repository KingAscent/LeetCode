class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int row = matrix.length;
        int col = matrix[0].length;
        int i = 0;
        int j = col - 1;

        while(i < row && 0 <= j){
            if(matrix[i][j] == target)
                return true;
            else if(target < matrix[i][j])
                j--;
            else
                i++;
        }

        return false;
    }
}
