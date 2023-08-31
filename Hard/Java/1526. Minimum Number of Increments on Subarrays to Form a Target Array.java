class Solution {
    public int minNumberOperations(int[] target) {
        int ops = 0;
        int prev = 0;

        for(int n : target){
            if(prev < n)
                ops += n - prev;
            prev = n;
        }

        return ops;
    }
}
