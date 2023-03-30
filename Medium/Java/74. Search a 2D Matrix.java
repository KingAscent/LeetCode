class Solution {
    public boolean searchMatrix(int[][] matrix, int target) {
        int r = matrix.length;
        int c = matrix[0].length;
        int i = 0;
        int j = c - 1;

        while(0 <= i && i < r && 0 <= j && j < c){
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
