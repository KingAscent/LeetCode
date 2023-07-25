class Solution {
    public int peakIndexInMountainArray(int[] arr) {
        int left = 0;
        int right = arr.length - 1;

        while(left < right){
            int temp = (left + right) / 2;
            if(arr[temp] < arr[temp + 1])
                left = temp + 1;
            else
                right = temp;
        }

        return left;
    }
}
