class Solution {
    public int maxCount(int m, int n, int[][] ops) {
        int r = m;
        int c = n;

        for(int[] i : ops){
            r = Math.min(r, i[0]);
            c = Math.min(c, i[1]);
        }

        return r * c;
    }
}
