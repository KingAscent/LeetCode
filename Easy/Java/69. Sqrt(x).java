class Solution {
    public int mySqrt(int x) {
        long root = x;

        while(x < root * root){
            root = (root + x / root) / 2;
        }

        return (int)root;
    }
}
