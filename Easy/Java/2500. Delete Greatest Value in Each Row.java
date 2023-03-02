class Solution {
    public int deleteGreatestValue(int[][] grid) {
        int sum = 0;

        for(int[] i : grid){
            Arrays.sort(i);
        }

        for(int i = 0; i < grid[0].length; i++){
            int max = 0;
            for(int[] e : grid){
                if(max <= e[i])
                    max = e[i];
            }
            sum += max;
        }

        return sum;
    }
}
