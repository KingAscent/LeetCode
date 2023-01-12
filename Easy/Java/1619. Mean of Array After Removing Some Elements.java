class Solution {
    public double trimMean(int[] arr) {
        int sum = 0;
        int fivePercent = arr.length / 20;
        Arrays.sort(arr);

        for(int i = fivePercent; i < arr.length - fivePercent; i++){
            sum += arr[i];
        }

        return (sum * 1.0) / (arr.length - (2 * fivePercent));
    }
}
