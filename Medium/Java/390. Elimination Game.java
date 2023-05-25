class Solution {
    public int lastRemaining(int n) {
        int last = 1;
        if(n == 1){
            return last;
        }else{
            int temp = lastRemaining(n / 2);
            last = 2 * ((n / 2) - temp + 1);
        }
        return last;
    }
}
