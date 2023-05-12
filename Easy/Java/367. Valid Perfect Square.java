class Solution {
    public boolean isPerfectSquare(int num) {
        int i = 1;
        while(0 < num){
            num -= i;
            i += 2;
        }
        return num == 0;
    }
}
