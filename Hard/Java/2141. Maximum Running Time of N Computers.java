class Solution {
    public long maxRunTime(int n, int[] batteries) {
        Arrays.sort(batteries);
        long sum = 0;
        int k = 0;
        int len = batteries.length;

        for(int b : batteries)
            sum += b;

        while(sum / (n - k) < batteries[len - 1 - k]){
            sum -= batteries[len - 1 - k];
            k++;
        }
        
        return sum / (n - k);
    }
}
