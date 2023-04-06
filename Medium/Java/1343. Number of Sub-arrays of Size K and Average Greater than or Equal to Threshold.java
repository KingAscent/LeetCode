class Solution {
    public int numOfSubarrays(int[] arr, int k, int threshold) {
        int count = 0;
        int sum = 0;
        int avg = 0;

        for(int i = 0; i < arr.length; i++){
            sum += arr[i];
            if(k - 1 <= i){
                avg = sum / k;
                if(threshold <= avg)
                    count++;
                sum -= arr[i - (k - 1)];
            }
        }

        return count;
    }
}
