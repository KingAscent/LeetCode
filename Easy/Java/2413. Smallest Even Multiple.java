class Solution {
    public int smallestEvenMultiple(int n) {
        int min = n * 2;
        if(n % 2 == 0)
            min = n;
        return min;
    }
}
