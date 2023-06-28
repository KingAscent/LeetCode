class Solution {
    public int minOperations(int n) {
        int count = 0;

        for(int i = (2 * n - 2) / 2; 0 <= i; i -= 2)
            count += i;
            
        return count;
    }
}
