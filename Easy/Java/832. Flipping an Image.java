class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for(int[] col : image){
            int i = 0;
            int j = image.length - 1;
            
            while(i <= j){
                int temp = col[i];
                col[i++] = 1 - col[j];
                col[j--] = 1 - temp;
            }
        }

        return image;
    }
}
