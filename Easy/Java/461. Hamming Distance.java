class Solution {
    public int hammingDistance(int x, int y) {
        int num = 0;

        while(0 < x || 0 < y){
            if(x % 2 != y % 2)
                num++;
            x /= 2;
            y /= 2;
        }

        return num;
    }
}
