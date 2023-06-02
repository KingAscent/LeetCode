class Solution {
    public List<Integer> spiralOrder(int[][] matrix) {
        int top = 0;
        int bot = matrix.length - 1;
        int left = 0;
        int right = matrix[0].length - 1;
        List<Integer> spiral = new ArrayList<>();

        // Find all the elements of the matrix in spiral order
        while(top <= bot && left <= right){
            // Top row
            for(int i = left; i <= right; i++)
                spiral.add(matrix[top][i]);
            top++;

            // Right column
            for(int i = top; i <= bot; i++)
                spiral.add(matrix[i][right]);
            right--;

            // Bottom row
            if(top <= bot){
                for(int i = right; left <= i; i--)
                    spiral.add(matrix[bot][i]);
                bot--;
            }

            // Left column
            if(left <= right){
                for(int i = bot; top <= i; i--)
                    spiral.add(matrix[i][left]);
                left++;
            }
        }

        return spiral;
    }
}
