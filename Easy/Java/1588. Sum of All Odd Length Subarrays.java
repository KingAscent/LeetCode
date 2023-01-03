class Solution {
    public int sumOddLengthSubarrays(int[] arr) {
        int sum = 0;

        // Count each element in an odd-length sub-array and multiply
        // the array elements to get the output of the sum
        for(int i = 0; i < arr.length; i++){
            int present = ((i + 1) * (arr.length - i) + 1) / 2;
            sum += present * arr[i];
        }

        return sum;
    }
}
